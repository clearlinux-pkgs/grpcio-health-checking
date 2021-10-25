#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio-health-checking
Version  : 1.41.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/eb/0f/c4b2d01d1ee0332e818c7774bc993c33811272351bb86f992523d7371115/grpcio-health-checking-1.41.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/eb/0f/c4b2d01d1ee0332e818c7774bc993c33811272351bb86f992523d7371115/grpcio-health-checking-1.41.1.tar.gz
Summary  : Standard Health Checking Service for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: grpcio-health-checking-license = %{version}-%{release}
Requires: grpcio-health-checking-python = %{version}-%{release}
Requires: grpcio-health-checking-python3 = %{version}-%{release}
Requires: grpcio
Requires: protobuf
BuildRequires : buildreq-distutils3
BuildRequires : grpcio
BuildRequires : protobuf

%description
===========================
        
        Reference package for GRPC Python health checking.
        
        Supported Python Versions
        -------------------------
        Python >= 3.6
        
        Dependencies
        ------------
        
        Depends on the `grpcio` package, available from PyPI via `pip install grpcio`.

%package license
Summary: license components for the grpcio-health-checking package.
Group: Default

%description license
license components for the grpcio-health-checking package.


%package python
Summary: python components for the grpcio-health-checking package.
Group: Default
Requires: grpcio-health-checking-python3 = %{version}-%{release}

%description python
python components for the grpcio-health-checking package.


%package python3
Summary: python3 components for the grpcio-health-checking package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_health_checking)
Requires: pypi(grpcio)
Requires: pypi(protobuf)

%description python3
python3 components for the grpcio-health-checking package.


%prep
%setup -q -n grpcio-health-checking-1.41.1
cd %{_builddir}/grpcio-health-checking-1.41.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635204386
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
mkdir -p %{buildroot}/usr/share/package-licenses/grpcio-health-checking
cp %{_builddir}/grpcio-health-checking-1.41.1/LICENSE %{buildroot}/usr/share/package-licenses/grpcio-health-checking/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grpcio-health-checking/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
