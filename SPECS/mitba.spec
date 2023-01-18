%global srcname mitba

Name:          python3-%{srcname}
Version:       1.1.1
Release:       1%{?dist}
Summary:       Python library for caching results from functions and methods
License:       BSD
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-flux
Requires:      python3-logbook >= 0.12.2

%description
Mitba is a small library for implementing method
or function-level caching for results.

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.1.1-1
- Initial RPM release
