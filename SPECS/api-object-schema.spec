%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname api_object_schema
%global pkgname api-object-schema

Name:          python%{python3_pkgversion}-%{pkgname}
Version:       2.0.0
Release:       1%{?tag}%{?dist}
Summary:       API Object Schema
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
Requires:      python%{python3_pkgversion}dist(sentinels)

%description
API Object Schema is a library of utilities for defining
schemas of Pythonic objects interacting with external APIs.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
for src in LICENSE README.md; do
    curl -fsSLO https://raw.githubusercontent.com/Infinidat/%{srcname}/%{version}/$src
done

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.0.0-1
- Initial RPM release
