%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname pact

Name:          python%{python3_pkgversion}-%{srcname}
Version:       1.12.0
Release:       1%{?tag}%{?dist}
Summary:       Promises library in Python
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
Requires:      python%{python3_pkgversion}dist(flux)
Requires:      python%{python3_pkgversion}dist(logbook) >= 0.12.2
Requires:      python%{python3_pkgversion}dist(waiting)

%description
Pact is a library implementing a general concept of promises/deferreds.
It less strictly follows known standards such as A+, but rather aims
to be practical for library or framework implementations.

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.12.0-1
- Initial RPM release
