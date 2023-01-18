%global srcname URLObject
%global pkgname urlobject

Name:          python3-%{pkgname}
Version:       2.4.3
Release:       1%{?dist}
Summary:       A utility class for manipulating URLs
License:       Public Domain
URL:           https://github.com/zacharyvoase/%{pkgname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
URLObject is a utility class for manipulating URLs.
The latest incarnation of this library builds upon
the ideas of its predecessor, but aims for a clearer API,
focusing on proper method names over operator overrides. 

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license UNLICENSE
%doc README.rst
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.4.3-1
- Initial RPM release
