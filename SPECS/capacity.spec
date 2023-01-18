%global srcname capacity

Name:          python3-%{srcname}
Version:       1.3.14
Release:       1%{?dist}
Summary:       Data types to describe capacity
License:       BSD
URL:           https://github.com/vmalloc/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Capacity is a package helping you express capacity (or data size)units
as Pythonic objects, and manipulate them in a useful, intuitive manner.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
curl -fsSLO https://raw.githubusercontent.com/vmalloc/%{srcname}/%{version}/LICENSE

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.3.14-1
- Initial RPM release
