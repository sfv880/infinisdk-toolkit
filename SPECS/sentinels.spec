%global srcname sentinels

Name:          python3-%{srcname}
Version:       1.0.0
Release:       1%{?dist}
Summary:       Various objects to denote special meanings in python
License:       BSD
URL:           https://github.com/vmalloc/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The sentinels module is a small utility providing the Sentinel class,
along with useful instances.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.0.0-1
- Initial RPM release
