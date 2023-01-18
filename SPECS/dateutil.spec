%global srcname python-dateutil
%global dstname python_dateutil
%global pkgname dateutil

Name:          python3-%{pkgname}
Version:       2.8.2
Release:       1%{?dist}
Epoch:         1
Summary:       Extensions to the standard Python datetime module
License:       BSD
URL:           https://github.com/dateutil/%{pkgname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
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
