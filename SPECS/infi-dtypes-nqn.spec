%global srcname infi.dtypes.nqn
%global pkgname infi-dtypes-nqn

Name:          python3-%{pkgname}
Version:       0.1.0
Release:       1%{?dist}
Summary:       NQN datatype NVMe-oF
License:       Python
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
NQN datatype in Python Datatype for NVMe-oF NQN in Python.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
curl -fsSLO https://raw.githubusercontent.com/python/cpython/main/LICENSE
curl -fsSLO https://raw.githubusercontent.com/Infinidat/%{srcname}/v0.1/README.md

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/infi/dtypes/nqn
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Fri Apr 11 2025 Alexander Deiter <adeiter@infinidat.com> - 0.1.0-1
- Initial RPM release
