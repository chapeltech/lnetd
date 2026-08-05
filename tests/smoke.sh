#!/bin/sh

set -eu

tmpdir=$(mktemp -d)
socket=$tmpdir/lnetd.sock
pid=

cleanup()
{
	if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
		kill "$pid"
		wait "$pid" || :
	fi
	rm -rf "$tmpdir"
}
trap cleanup EXIT HUP INT TERM

setsid ./lnetd -d "$socket" /bin/cat >"$tmpdir/lnetd.log" 2>&1 &
pid=$!

i=0
while [ ! -S "$socket" ] && [ "$i" -lt 50 ]; do
	sleep 0.1
	i=$((i + 1))
done

if [ ! -S "$socket" ]; then
	cat "$tmpdir/lnetd.log" >&2
	echo "lnetd did not create its socket" >&2
	exit 1
fi

python3 - "$socket" <<'PY'
import socket
import sys

message = b"lnetd smoke test\n"

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
    client.settimeout(5)
    client.connect(sys.argv[1])
    client.sendall(message)
    client.shutdown(socket.SHUT_WR)

    reply = b""
    while True:
        data = client.recv(4096)
        if not data:
            break
        reply += data

if reply != message:
    raise SystemExit(f"unexpected reply: {reply!r}")
PY
