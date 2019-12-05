#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-build
Version  : 0.10.0
Release  : 25
URL      : https://github.com/scikit-build/scikit-build/archive/0.10.0/scikit-build-0.10.0.tar.gz
Source0  : https://github.com/scikit-build/scikit-build/archive/0.10.0/scikit-build-0.10.0.tar.gz
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
BuildRequires : packaging
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : wheel

%description
This folder contains files the define CMake's defaults for given platforms.  Any of them can be overridden by either
command line or by environment variables.

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
%setup -q -n scikit-build-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558939416
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
