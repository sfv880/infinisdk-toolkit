%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname infinisdk

Name:          python%{python3_pkgversion}-%{srcname}
Version:       258.0.2
Release:       1%{?tag}%{?dist}
Summary:       Infinidat API SDK
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pbr)
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
Requires:      python%{python3_pkgversion}dist(api-object-schema) >= 1.5.1
Requires:      python%{python3_pkgversion}dist(arrow) >= 0.6.0
Requires:      python%{python3_pkgversion}dist(capacity) >= 1.3.8
Requires:      python%{python3_pkgversion}dist(click) >= 8.0.4
Requires:      python%{python3_pkgversion}dist(colorama)
Requires:      python%{python3_pkgversion}dist(confetti) >= 2.1.0
Requires:      python%{python3_pkgversion}dist(flux)
Requires:      python%{python3_pkgversion}dist(gossip) >= 2.3.1
Requires:      python%{python3_pkgversion}dist(infi.dtypes.iqn) >= 0.4
Requires:      python%{python3_pkgversion}dist(infi.dtypes.nqn) >= 0.1
Requires:      python%{python3_pkgversion}dist(infi.dtypes.wwn) >= 0.1
Requires:      python%{python3_pkgversion}dist(logbook) >= 0.11.0
Requires:      python%{python3_pkgversion}dist(mitba)
Requires:      python%{python3_pkgversion}dist(munch)
Requires:      python%{python3_pkgversion}dist(pact) >= 1.0.0
Requires:      python%{python3_pkgversion}dist(python-dateutil)
Requires:      python%{python3_pkgversion}dist(requests) >= 2.4.0
Requires:      python%{python3_pkgversion}dist(sentinels)
Requires:      python%{python3_pkgversion}dist(storage-interfaces)
Requires:      python%{python3_pkgversion}dist(urlobject)
Requires:      python%{python3_pkgversion}dist(vintage) >= 0.4.0

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
