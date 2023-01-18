%global srcname infi.dtypes.wwn
%global pkgname infi-dtypes-wwn

Name:          python3-%{pkgname}
Version:       0.1.1
Release:       1%{?dist}
Summary:       Datatype for WWN
License:       Python
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python3-devel
BuildRequires: python3-setuptools

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
