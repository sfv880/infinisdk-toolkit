%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname Logbook
%global pkgname logbook

Name:          python%{python3_pkgversion}-%{pkgname}
Version:       1.5.3
Release:       1%{?tag}%{?dist}
Summary:       A logging replacement for Python
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/getlogbook/%{pkgname}
Source:        %{pypi_source}

BuildRequires: gcc
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(cython)
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)

%description
Logbook is a logging system for Python that replaces the standard library's
logging module. It was designed with both complex and simple applications
and mind and the idea to make logging fun.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
cython-%{python3_pkgversion} %{pkgname}/_speedups.pyx
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
