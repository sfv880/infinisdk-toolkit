%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname arrow

Name:          python%{python3_pkgversion}-%{srcname}
Version:       0.15.8
Release:       1%{?tag}%{?dist}
Summary:       Better dates & times for Python
Group:         Applications/System
License:       ASL 2.0
Vendor:        Infinidat
URL:           https://github.com/arrow-py/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
BuildRequires: python%{python3_pkgversion}dist(six)
Requires:      python%{python3_pkgversion}dist(python-dateutil)
Requires:      python%{python3_pkgversion}dist(six)

%description
Arrow is a Python library that offers a sensible and human-friendly
approach to creating, manipulating, formatting and converting dates,
times and timestamps. It implements and updates the datetime type,
plugging gaps in functionality and providing an intelligent module
API that supports many common creation scenarios.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 0.15.8-1
- Initial RPM release
