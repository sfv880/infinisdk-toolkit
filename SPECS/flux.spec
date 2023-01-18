%global srcname flux

Name:          python3-%{srcname}
Version:       1.3.5
Release:       1%{?dist}
Summary:       Artificial time library
License:       BSD
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-pbr
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Flux is a Python library enabling you to create virtual
timelines and use them to test long processes.

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.3.5-1
- Initial RPM release
