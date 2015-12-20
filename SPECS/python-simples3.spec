%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname simples3
%global __pip pip-python

Name:           python-%{srcname}
Version:        1.0
Release:        1.vortex%{?dist}
Summary:        Fairly simple, decently quick interface to Amazon’s S3 storage service
Vendor:         Vortex RPM

Group:          Development/Libraries
License:        MIT
URL:            http://sendapatch.se/projects/simples3/
Source0:        http://pypi.python.org/packages/source/p/pip/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools, python-devel

%description
daemonize is a library for writing system daemons in Python. It has some bits
from daemonize.sourceforge.net. It is distributed under MIT license.

Simple, quick Amazon AWS S3 interface

simples3 is a fairly simple, decently quick interface to Amazon’s S3 storage
service.

It grew out of frustration with other libraries that were either written too
pragmatically (slow), too bloatedly, or just half-done.

The module aims for:

- simplicity,
- decent speed,
- non-intrusiveness.

It really is designed to fit into programmer memory. The three basic
operations are as easy as with dictionaries.

Out of simplicity comes no dependencies - the code relies solely on Python
standard libraries.

simples3 requires Python 2.5+ and nose for running tests. Python 3 support
is not yet available.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE TODO changes.rst
%{python_sitelib}/%{srcname}*

%changelog
* Sun Dec 20 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.0-1.vortex
- Initial packaging.
