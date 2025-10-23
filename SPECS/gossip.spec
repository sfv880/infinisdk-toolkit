%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname gossip

Name:          python%{python3_pkgversion}-%{srcname}
Version:       2.4.0
Release:       1%{?tag}%{?dist}
Summary:       Signaling and hooking library
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pbr)
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
Requires:      python%{python3_pkgversion}dist(logbook) >= 0.12.0
Requires:      python%{python3_pkgversion}dist(sentinels)
Requires:      python%{python3_pkgversion}dist(vintage) >= 0.4.0

%description
Gossip is a library implementing a basic hook mechanism for
implementing callbacks. It provides flexible configuration,
hook namespaces and error handling strategies.

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.4.0-1
- Initial RPM release
