%global srcname munch

Name:          python3-%{srcname}
Version:       2.5.0
Release:       1%{?dist}
Summary:       A dot-accessible dictionary (a la JavaScript objects)
License:       MIT
URL:           https://github.com/Infinidat/%{srcname}
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-pbr
BuildRequires: python3-pip
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Munch is a fork of David Schoonover's Bunch package, providing
similar functionality. 99% of the work was done by him, and
the fork was made mainly for lack of responsiveness for fixes
and maintenance on the original code. Munch is a dictionary
that supports attribute-style access, a la JavaScript.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 2.5.0-1
- Initial RPM release
