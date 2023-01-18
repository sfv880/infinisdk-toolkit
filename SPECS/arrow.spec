%global srcname arrow

Name:          python3-%{srcname}
Version:       0.15.8
Release:       1%{?dist}
Summary:       Better dates & times for Python
License:       ASL 2.0
URL:           https://github.com/arrow-py/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-six
Requires:      python3-dateutil
Requires:      python3-six

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
