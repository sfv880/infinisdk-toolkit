%global srcname click

Name:          python3-%{srcname}
Version:       8.0.4
Release:       1%{?dist}
Summary:       Composable command line interface toolkit
License:       BSD
URL:           https://github.com/pallets/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Click is a Python package for creating beautiful command line
interfacesin a composable way with as little code as necessary.
It's the "Command Line Interface Creation Kit". It's highly
configurable but comes with sensible defaults out of the box.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
echo '# Marker file for PEP 561. The mypy package uses inline types.' | \
    tee src/click/py.typed

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.rst
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 8.0.4-1
- Initial RPM release
