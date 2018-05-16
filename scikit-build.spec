#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA50C0312039D473C (jcfr@protonmail.ch)
#
Name     : scikit-build
Version  : 0.6.1
Release  : 10
URL      : https://github.com/scikit-build/scikit-build/releases/download/0.6.1/scikit-build-0.6.1.tar.gz
Source0  : https://github.com/scikit-build/scikit-build/releases/download/0.6.1/scikit-build-0.6.1.tar.gz
Source99 : https://github.com/scikit-build/scikit-build/releases/download/0.6.1/scikit-build-0.6.1.tar.gz.asc
Summary  : Improved build system generator for Python C extensions
Group    : Development/Tools
License  : MIT NCSA
Requires: scikit-build-python3
Requires: scikit-build-python
Requires: setuptools
Requires: wheel
BuildRequires : cmake
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
scikit-build
        ===============================
        
        Improved build system generator for CPython C extensions.
        
        Better support is available for additional compilers, build systems, cross
        compilation, and locating dependencies and determining their build
        requirements. The **scikit-build** package is fundamentally just glue between

%package legacypython
Summary: legacypython components for the scikit-build package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the scikit-build package.


%package python
Summary: python components for the scikit-build package.
Group: Default
Requires: scikit-build-python3

%description python
python components for the scikit-build package.


%package python3
Summary: python3 components for the scikit-build package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scikit-build package.


%prep
%setup -q -n scikit-build-0.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519360155
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519360155
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
