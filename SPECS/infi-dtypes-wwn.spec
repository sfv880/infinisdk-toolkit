%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname infi.dtypes.wwn
%global pkgname infi-dtypes-wwn

Name:          python%{python3_pkgversion}-%{pkgname}
Version:       0.1.1
Release:       1%{?tag}%{?dist}
Summary:       Datatype for WWN
Group:         Applications/System
License:       Python
Vendor:        Infinidat
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)

%description
Infi.dtypes.wwn provides a datatype for representing WWNs
from strings in various formats.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
curl -fsSLO https://raw.githubusercontent.com/python/cpython/main/LICENSE

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/infi/dtypes/wwn
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 0.1.1-1
- Initial RPM release
