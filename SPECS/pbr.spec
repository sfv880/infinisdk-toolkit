%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname pbr

Name:          python%{python3_pkgversion}-%{srcname}
Version:       7.0.1
Release:       1%{?tag}%{?dist}
Summary:       Python Build Reasonableness
Group:         Applications/System
License:       ASL 2.0
Vendor:        Infinidat
URL:           https://pypi.org/project/pbr
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)

%description
PBR is a library that injects some useful and sensible default behaviors into
your setuptools run. It started off life as the chunks of code that were copied
between all of the OpenStack projects. Around the time that OpenStack hit 18
different projects each with at least 3 active branches, it seems like a good
time to make that code into a proper re-usable library.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{_bindir}/pbr
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 21 2025 Alexander Deiter <adeiter@infinidat.com> - 7.0.1-1
- Initial RPM release
