%global srcname infinisdk

Name:          python3-%{srcname}
Version:       258.0.2
Release:       1%{?dist}
Summary:       Infinidat API SDK
License:       BSD
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-pbr
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-api-object-schema >= 1.5.1
Requires:      python3-arrow >= 0.6.0
Requires:      python3-capacity >= 1.3.8
Requires:      python3-click >= 8.0.4
Requires:      python3-colorama
Requires:      python3-confetti >= 2.1.0
Requires:      python3-dateutil
Requires:      python3-flux
Requires:      python3-gossip >= 2.3.1
Requires:      python3-infi-dtypes-iqn >= 0.3.0
Requires:      python3-infi-dtypes-nqn >= 0.1.0
Requires:      python3-infi-dtypes-wwn >= 0.0.2
Requires:      python3-logbook >= 0.11.0
Requires:      python3-mitba
Requires:      python3-munch
Requires:      python3-pact >= 1.0.0
Requires:      python3-requests >= 2.4.0
Requires:      python3-sentinels
Requires:      python3-storage-interfaces
Requires:      python3-urlobject
Requires:      python3-vintage >= 0.4.0

%description
InfiniSDK is the official Python SDK for INFINIDAT's products.
It provides a clean interface for creating, deleting, querying
and manipulating API objects.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}/%{_bindir}/%{srcname}-cli

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 11 2025 Alexander Deiter <adeiter@infinidat.com> - 258.0.2-1
- Bump version 206.1.2 => 258.0.2
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 185.1.1-1
- Initial RPM release
