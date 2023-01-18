%global srcname waiting

Name:          python3-%{srcname}
Version:       1.4.1
Release:       1%{?dist}
Summary:       Utility for waiting for stuff to happen
License:       BSD
URL:           https://github.com/vmalloc/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Waiting is a small library for waiting for stuff to happen.
It basically waits for a function to return True, in various modes.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
curl -fsSLO https://raw.githubusercontent.com/vmalloc/%{srcname}/%{version}/LICENSE

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.4.1-1
- Initial RPM release
