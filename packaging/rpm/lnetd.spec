Name:           lnetd
Version:        0.3
Release:        2%{?dist}
Summary:        Lightweight inetd-style listener
License:        MIT
URL:            https://github.com/ChapelTech/lnetd
Source0:        lnetd-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  groff-base
BuildRequires:  python3
BuildRequires:  util-linux

%description
lnetd is a small inetd-style network listener.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}" NROFF=/usr/bin/nroff

%check
%make_build check

%install
install -Dpm0755 lnetd %{buildroot}%{_sbindir}/lnetd
install -Dpm0644 lnetd.8 %{buildroot}%{_mandir}/man8/lnetd.8

%files
%license debian/copyright
%{_sbindir}/lnetd
%{_mandir}/man8/lnetd.8*

%changelog
* Thu Aug 06 2026 ChapelTech <packages@chapel.tech> - 0.3-2
- Release 0.3 with Debian, EL9, and Alpine package automation.

* Wed Aug 05 2026 ChapelTech <packages@chapel.tech> - 0.2-2
- Rebuild for Debian 13 and add signed EL9 release automation.

* Wed Aug 05 2026 ChapelTech <packages@chapel.tech> - 0.2-1
- Add Rocky/RHEL packaging.
