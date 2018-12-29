#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-build
Version  : 0.8.1
Release  : 20
URL      : https://github.com/scikit-build/scikit-build/archive/0.8.1.tar.gz
Source0  : https://github.com/scikit-build/scikit-build/archive/0.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : NCSA
Requires: scikit-build-license = %{version}-%{release}
Requires: scikit-build-python = %{version}-%{release}
Requires: scikit-build-python3 = %{version}-%{release}
Requires: packaging
Requires: setuptools
Requires: wheel
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
scikit-build
===============================
Improved build system generator for CPython C/C++/Fortran/Cython extensions.

%package license
Summary: license components for the scikit-build package.
Group: Default

%description license
license components for the scikit-build package.


%package python
Summary: python components for the scikit-build package.
Group: Default
Requires: scikit-build-python3 = %{version}-%{release}

%description python
python components for the scikit-build package.


%package python3
Summary: python3 components for the scikit-build package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scikit-build package.


%prep
%setup -q -n scikit-build-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540771994
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scikit-build
cp LICENSE %{buildroot}/usr/share/package-licenses/scikit-build/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scikit-build/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
