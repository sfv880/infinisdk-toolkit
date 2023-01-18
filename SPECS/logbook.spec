%global srcname Logbook
%global pkgname logbook

Name:          python3-%{pkgname}
Version:       1.5.3
Release:       1%{?dist}
Summary:       A logging replacement for Python
License:       BSD
URL:           https://github.com/getlogbook/%{pkgname}
Source:        %{pypi_source}

BuildRequires: gcc
BuildRequires: python3-Cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Logbook is a logging system for Python that replaces the standard library's
logging module. It was designed with both complex and simple applications
and mind and the idea to make logging fun.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
cython %{pkgname}/_speedups.pyx
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pkgname}
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.5.3-1
- Initial RPM release
