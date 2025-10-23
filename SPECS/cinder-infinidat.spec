%global tag .infinidat
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python%{python3_pkgversion}
%global srcname powervc
%global project infinidat-powervc-cinder

Name:          python%{python3_pkgversion}-cinder-infinidat
Version:       2.3.1
Release:       1%{?tag}%{?dist}
Summary:       Infinidat OpenStack Cinder Volume Driver
Group:         Applications/System
License:       ASL 2.0
Vendor:        Infinidat
URL:           https://github.com/%{vendor}/%{project}
Source:        https://github.com/%{vendor}/%{project}/archive/%{srcname}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(pip)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
Requires:      python%{python3_pkgversion}dist(infinisdk) >= 258.0.2

%description
INFINIDAT InfiniBox Cinder Volume Driver for PowerVC

%prep
%autosetup -n %{project}-%{srcname}-%{version}

%install
install -v -d -m 0755 %{buildroot}%{python3_sitelib}/cinder/volume/drivers
install -v -m 0644 infinidat.py %{buildroot}%{python3_sitelib}/cinder/volume/drivers

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/cinder/volume/drivers

%changelog
* Wed Oct 22 2025 Alexander Deiter <adeiter@infinidat.com> - 2.3.1-1
- Initial RPM release
