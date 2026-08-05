Name:           lnetd
Version:        0.2
Release:        1%{?dist}
Summary:        Lightweight inetd-style listener
License:        MIT
URL:            https://github.com/elric1/lnetd
Source0:        lnetd-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  groff-base

%description
lnetd is a small inetd-style network listener.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}" NROFF=/usr/bin/nroff

%install
install -Dpm0755 lnetd %{buildroot}%{_sbindir}/lnetd
install -Dpm0644 lnetd.8 %{buildroot}%{_mandir}/man8/lnetd.8

%files
%license debian/copyright
%{_sbindir}/lnetd
%{_mandir}/man8/lnetd.8*

%changelog
* Wed Aug 05 2026 ChapelTech <packages@chapel.tech> - 0.2-1
- Add Rocky/RHEL packaging.
