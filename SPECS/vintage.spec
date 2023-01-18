%global srcname vintage

Name:          python3-%{srcname}
Version:       0.4.1
Release:       1%{?dist}
Summary:       Python library for deprecating code
License:       BSD
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Vintage is a library geared at making it easy to deprecate methods,
functions or other code elements in your projects. It emits nicely
formatted deprecation warnings, and helps you manage the deprecation
cycle easier.

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
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 0.4.1-1
- Initial RPM release
