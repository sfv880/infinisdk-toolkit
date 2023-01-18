%global srcname typing_extensions 
%global pkgname typing-extensions 

Name:          python3-%{pkgname}
Version:       3.10.0.2
Release:       1%{?dist}
Summary:       Backported and Experimental Type Hints for Python 3.6+
License:       Python
URL:           https://github.com/python/typing
Source:        %{pypi_source}

BuildArch:     noarch
BuildRequires: curl
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The typing module was added to the standard library in Python 3.5 on
a provisional basis and will no longer be provisional in Python 3.7.
However, this means users of Python 3.5 - 3.6 who are unable to
upgrade will not be able to take advantage of new types added to
the typing module, such as typing.Text or typing.Coroutine.
The typing_extensions module contains both backports of these changes
as well as experimental types that will eventually be added to the
typing module, such as Protocol (see PEP 544 for details about
protocols and static duck typing) or TypedDict (see PEP 589).

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%pycached %{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 04 2022 Alexander Deiter <adeiter@infinidat.com> - 3.10.0.2-1
- Initial RPM release
