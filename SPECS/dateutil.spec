%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname python-dateutil
%global dstname python_dateutil
%global pkgname dateutil

Name:          python%{python3_pkgversion}-%{pkgname}
Version:       2.8.2
Release:       1%{?tag}%{?dist}
Epoch:         1
Summary:       Extensions to the standard Python datetime module
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/dateutil/%{pkgname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
Requires:      tzdata

%description
The dateutil module provides powerful extensions to
the standard datetime module, available in Python.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc AUTHORS.md CONTRIBUTING.md README.rst
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{dstname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1:2.8.2-1
- Initial RPM release
