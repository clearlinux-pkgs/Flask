#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Flask
Version  : 1.1.1
Release  : 37
URL      : https://files.pythonhosted.org/packages/2e/80/3726a729de758513fd3dbc64e93098eb009c49305a97c6751de55b20b694/Flask-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/80/3726a729de758513fd3dbc64e93098eb009c49305a97c6751de55b20b694/Flask-1.1.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/2e/80/3726a729de758513fd3dbc64e93098eb009c49305a97c6751de55b20b694/Flask-1.1.1.tar.gz.asc
Summary  : A simple framework for building complex web applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Flask-bin = %{version}-%{release}
Requires: Flask-license = %{version}-%{release}
Requires: Flask-python = %{version}-%{release}
Requires: Flask-python3 = %{version}-%{release}
Requires: Flask
Requires: Jinja2
Requires: Werkzeug
Requires: click
Requires: itsdangerous
BuildRequires : Flask
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Werkzeug
BuildRequires : Werkzeug-python
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : itsdangerous
BuildRequires : itsdangerous-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Flask
=====
Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

%package bin
Summary: bin components for the Flask package.
Group: Binaries
Requires: Flask-license = %{version}-%{release}

%description bin
bin components for the Flask package.


%package license
Summary: license components for the Flask package.
Group: Default

%description license
license components for the Flask package.


%package python
Summary: python components for the Flask package.
Group: Default
Requires: Flask-python3 = %{version}-%{release}
Provides: flask-python

%description python
python components for the Flask package.


%package python3
Summary: python3 components for the Flask package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Flask package.


%prep
%setup -q -n Flask-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562637858
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Flask
cp LICENSE.rst %{buildroot}/usr/share/package-licenses/Flask/LICENSE.rst
cp examples/javascript/LICENSE %{buildroot}/usr/share/package-licenses/Flask/examples_javascript_LICENSE
cp examples/tutorial/LICENSE %{buildroot}/usr/share/package-licenses/Flask/examples_tutorial_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flask

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Flask/LICENSE.rst
/usr/share/package-licenses/Flask/examples_javascript_LICENSE
/usr/share/package-licenses/Flask/examples_tutorial_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
