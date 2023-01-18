%global srcname confetti

Name:          python3-%{srcname}
Version:       2.5.3
Release:       1%{?dist}
Summary:       Generic configuration mechanism
License:       BSD
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-sentinels
Requires:      python3-six

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
