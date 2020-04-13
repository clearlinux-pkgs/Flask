#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Flask
Version  : 1.1.2
Release  : 40
URL      : https://files.pythonhosted.org/packages/4e/0b/cb02268c90e67545a0e3a37ea1ca3d45de3aca43ceb7dbf1712fb5127d5d/Flask-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/0b/cb02268c90e67545a0e3a37ea1ca3d45de3aca43ceb7dbf1712fb5127d5d/Flask-1.1.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/4e/0b/cb02268c90e67545a0e3a37ea1ca3d45de3aca43ceb7dbf1712fb5127d5d/Flask-1.1.2.tar.gz.asc
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
=====
        
        Flask is a lightweight `WSGI`_ web application framework. It is designed
        to make getting started quick and easy, with the ability to scale up to
        complex applications. It began as a simple wrapper around `Werkzeug`_
        and `Jinja`_ and has become one of the most popular Python web
        application frameworks.
        
        Flask offers suggestions, but doesn't enforce any dependencies or
        project layout. It is up to the developer to choose the tools and
        libraries they want to use. There are many extensions provided by the
        community that make adding new functionality easy.
        
        
        Installing
        ----------

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
%setup -q -n Flask-1.1.2
cd %{_builddir}/Flask-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586815842
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Flask
cp %{_builddir}/Flask-1.1.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/Flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c
cp %{_builddir}/Flask-1.1.2/examples/javascript/LICENSE %{buildroot}/usr/share/package-licenses/Flask/42dd5ee1eb8465027fad79f01df54ad8c3ffba65
cp %{_builddir}/Flask-1.1.2/examples/tutorial/LICENSE %{buildroot}/usr/share/package-licenses/Flask/42dd5ee1eb8465027fad79f01df54ad8c3ffba65
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
/usr/share/package-licenses/Flask/42dd5ee1eb8465027fad79f01df54ad8c3ffba65
/usr/share/package-licenses/Flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
