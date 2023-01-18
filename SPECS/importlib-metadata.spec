%global srcname importlib_metadata
%global pkgname importlib-metadata

Name:          python3-%{pkgname}
Version:       4.8.3
Release:       1%{?dist}
Summary:       Read metadata from Python packages
License:       ASL
URL:           https://github.com/python/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Library to access the metadata for a Python package.
This package supplies third-party access to the
functionality of importlib.metadata including
improvements added to subsequent Python versions.

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
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 4.8.3-1
- Initial RPM release
