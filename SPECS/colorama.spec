%global srcname colorama

Name:          python3-%{srcname}
Version:       0.4.5
Release:       1%{?dist}
Summary:       Cross-platform colored terminal text
License:       BSD
URL:           https://github.com/tartley/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

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
