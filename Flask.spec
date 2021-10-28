#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Flask
Version  : 2.0.2
Release  : 46
URL      : https://files.pythonhosted.org/packages/95/40/b976286b5e7ba01794a7e7588e7e7fa27fb16c6168fa849234840bf0f61d/Flask-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/40/b976286b5e7ba01794a7e7588e7e7fa27fb16c6168fa849234840bf0f61d/Flask-2.0.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/95/40/b976286b5e7ba01794a7e7588e7e7fa27fb16c6168fa849234840bf0f61d/Flask-2.0.2.tar.gz.asc
Summary  : A simple framework for building complex web applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Flask-bin = %{version}-%{release}
Requires: Flask-license = %{version}-%{release}
Requires: Flask-python = %{version}-%{release}
Requires: Flask-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Werkzeug
Requires: asgiref
Requires: click
Requires: itsdangerous
Requires: python-dotenv
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Werkzeug
BuildRequires : Werkzeug-python
BuildRequires : asgiref
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : itsdangerous
BuildRequires : itsdangerous-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dotenv
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
Provides: pypi(flask)
Requires: pypi(click)
Requires: pypi(itsdangerous)
Requires: pypi(jinja2)
Requires: pypi(werkzeug)

%description python3
python3 components for the Flask package.


%prep
%setup -q -n Flask-2.0.2
cd %{_builddir}/Flask-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633379056
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Flask
cp %{_builddir}/Flask-2.0.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/Flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c
cp %{_builddir}/Flask-2.0.2/docs/license.rst %{buildroot}/usr/share/package-licenses/Flask/4747036caafe4df836d096b9b49d7fdb2782b0ff
cp %{_builddir}/Flask-2.0.2/examples/javascript/LICENSE.rst %{buildroot}/usr/share/package-licenses/Flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c
cp %{_builddir}/Flask-2.0.2/examples/tutorial/LICENSE.rst %{buildroot}/usr/share/package-licenses/Flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c
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
/usr/share/package-licenses/Flask/4747036caafe4df836d096b9b49d7fdb2782b0ff
/usr/share/package-licenses/Flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
