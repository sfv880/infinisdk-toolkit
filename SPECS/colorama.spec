%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname colorama

Name:          python%{python3_pkgversion}-%{srcname}
Version:       0.4.5
Release:       1%{?tag}%{?dist}
Summary:       Cross-platform colored terminal text
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/tartley/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)

%description
Colorama makes ANSI escape character sequences for producing
colored terminal text and cursor positioning.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 0.4.5-1
- Initial RPM release
