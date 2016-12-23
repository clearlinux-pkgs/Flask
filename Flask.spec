#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Flask
Version  : 0.11.1
Release  : 20
URL      : http://pypi.debian.net/Flask/Flask-0.11.1.tar.gz
Source0  : http://pypi.debian.net/Flask/Flask-0.11.1.tar.gz
Summary  : A microframework based on Werkzeug, Jinja2 and good intentions
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Flask-bin
Requires: Flask-python
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Werkzeug-python
BuildRequires : itsdangerous-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
// Flask //
web development, one drop at a time
~ What is Flask?
Flask is a microframework for Python based on Werkzeug
and Jinja2.  It's intended for getting started very quickly
and was developed with best intentions in mind.

%package bin
Summary: bin components for the Flask package.
Group: Binaries

%description bin
bin components for the Flask package.


%package python
Summary: python components for the Flask package.
Group: Default
Provides: flask-python
Requires: Jinja2
Requires: Werkzeug-python
Requires: itsdangerous-python

%description python
python components for the Flask package.


%prep
%setup -q -n Flask-0.11.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flask

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
