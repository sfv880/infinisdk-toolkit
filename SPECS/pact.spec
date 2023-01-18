%global srcname pact

Name:          python3-%{srcname}
Version:       1.12.0
Release:       1%{?dist}
Summary:       Promises library in Python
License:       BSD
URL:           https://github.com/getslash/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-pbr
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-flux
Requires:      python3-logbook >= 0.12.2
Requires:      python3-waiting

%description
Pact is a library implementing a general concept of promises/deferreds.
It less strictly follows known standards such as A+, but rather aims
to be practical for library or framework implementations.

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
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 1.12.0-1
- Initial RPM release
