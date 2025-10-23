%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname confetti

Name:          python%{python3_pkgversion}-%{srcname}
Version:       2.5.3
Release:       1%{?tag}%{?dist}
Summary:       Generic configuration mechanism
Group:         Applications/System
License:       BSD
Vendor:        Infinidat
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
Requires:      python%{python3_pkgversion}dist(sentinels)
Requires:      python%{python3_pkgversion}dist(six)

%description
Confetti is a Python library for dealing with hierarchical configuration data.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
curl -fsSLO https://raw.githubusercontent.com/getslash/%{srcname}/%{version}/LICENSE

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.5.3-1
- Initial RPM release
