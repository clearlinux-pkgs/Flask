#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Flask
Version  : 1.0.2
Release  : 31
URL      : https://files.pythonhosted.org/packages/4b/12/c1fbf4971fda0e4de05565694c9f0c92646223cff53f15b6eb248a310a62/Flask-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/12/c1fbf4971fda0e4de05565694c9f0c92646223cff53f15b6eb248a310a62/Flask-1.0.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/4b/12/c1fbf4971fda0e4de05565694c9f0c92646223cff53f15b6eb248a310a62/Flask-1.0.2.tar.gz.asc
Summary  : A simple framework for building complex web applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Flask-bin
Requires: Flask-python3
Requires: Flask-license
Requires: Flask-python
Requires: Jinja2
Requires: Werkzeug
Requires: click
Requires: itsdangerous
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Werkzeug
BuildRequires : Werkzeug-python
BuildRequires : buildreq-distutils3
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

%description python3
python3 components for the Flask package.


%prep
%setup -q -n Flask-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538839996
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/Flask
cp LICENSE %{buildroot}/usr/share/doc/Flask/LICENSE
cp artwork/LICENSE %{buildroot}/usr/share/doc/Flask/artwork_LICENSE
cp docs/license.rst %{buildroot}/usr/share/doc/Flask/docs_license.rst
cp examples/javascript/LICENSE %{buildroot}/usr/share/doc/Flask/examples_javascript_LICENSE
cp examples/tutorial/LICENSE %{buildroot}/usr/share/doc/Flask/examples_tutorial_LICENSE
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
/usr/share/doc/Flask/LICENSE
/usr/share/doc/Flask/artwork_LICENSE
/usr/share/doc/Flask/docs_license.rst
/usr/share/doc/Flask/examples_javascript_LICENSE
/usr/share/doc/Flask/examples_tutorial_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
