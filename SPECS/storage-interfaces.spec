%global srcname storage_interfaces
%global pkgname storage-interfaces

Name:          python3-%{pkgname}
Version:       1.0.4
Release:       1%{?dist}
Summary:       Abstract classes for representing storage-related objects
License:       BSD
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Abstract classes for representing storage-related objects.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.0.4-1
- Initial RPM release
