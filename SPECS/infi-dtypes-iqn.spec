%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname infi.dtypes.iqn
%global pkgname infi-dtypes-iqn

Name:          python%{python3_pkgversion}-%{pkgname}
Version:       0.4.0
Release:       1%{?tag}%{?dist}
Summary:       Datatype for IQN
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
IQN datatype in Python Datatype for iSCSI IQN in Python.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
curl -fsSLO https://raw.githubusercontent.com/python/cpython/main/LICENSE
curl -fsSLO https://raw.githubusercontent.com/Infinidat/%{srcname}/v%{version}/README.md

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/infi/dtypes/iqn
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 0.4.0-1
- Initial RPM release
