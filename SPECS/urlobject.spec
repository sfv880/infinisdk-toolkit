%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname URLObject
%global pkgname urlobject

Name:          python%{python3_pkgversion}-%{pkgname}
Version:       2.4.3
Release:       1%{?tag}%{?dist}
Summary:       A utility class for manipulating URLs
Group:         Applications/System
License:       Public Domain
Vendor:        Infinidat
URL:           https://github.com/zacharyvoase/%{pkgname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)

%description
URLObject is a utility class for manipulating URLs.
The latest incarnation of this library builds upon
the ideas of its predecessor, but aims for a clearer API,
focusing on proper method names over operator overrides. 

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license UNLICENSE
%doc README.rst
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.4.3-1
- Initial RPM release
