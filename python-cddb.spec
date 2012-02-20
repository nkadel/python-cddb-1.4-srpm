# $Id: python-cddb.spec,v 1.1 2012/02/19 21:55:54 nkadel Exp nkadel $
# Authority: dries

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

# Modern versions of RHEL and Fedora with python 2.6 install info file
%{?el4: %define _without_info 1}
%{?el5: %define _without_info 1}

%{?!_with_info: %{!?_without_info: %define _with_info 1}}
%{?_with_info: %{?_without_info: %{error: both _with_info and _without_info exist}}}
%{!?_with_info: %{!?_without_info: %{error: neither _with_info nor _without_info exist}}}

%define real_name CDDB

Summary: Fetch information about audio cd's
Name: python-cddb
Version: 1.4
Release: 2.1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://cddb-py.sourceforge.net/

Source: http://dl.sf.net/cddb-py/CDDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
Requires: python
Provides: python-CDDB = %{version}-%{release}
Obsoletes: python-CDDB <= %{version}-%{release}

%description
This is a set of three modules to access the CDDB and FreeDB online
databases of audio CD track titles and information.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{python_sitearch}/*.py
%{python_sitearch}/*.pyc
%ghost %{python_sitearch}/*.pyo
%{python_sitearch}/cdrom.so
%if %{?_with_info:1}%{!?_without_info:0}
%{python_sitearch}/CDDB-%{version}-*-info
%endif

%changelog
* Sun Feb 19 2012 Nico Kadel-Garcia <nkadel@gmail.com> - 1.4-2.1
- Add logic to include CDDB*-info file for Python 2.6 based RHEL

* Sat Jul 28 2007 Dag Wieers <dag@wieers.com> - 1.4-2
- Provides and obsoletes python-CDDB.

* Fri Mar 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
