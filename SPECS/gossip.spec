%global srcname gossip

Name:          python3-%{srcname}
Version:       2.4.0
Release:       1%{?dist}
Summary:       Signaling and hooking library
License:       BSD
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-logbook >= 0.12.0
Requires:      python3-sentinels
Requires:      python3-vintage >= 0.4.0

%description
Gossip is a library implementing a basic hook mechanism for
implementing callbacks. It provides flexible configuration,
hook namespaces and error handling strategies.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.4.0-1
- Initial RPM release
