
#
Summary:	X Damage extension library
Summary(pl):	Biblioteka rozszerzenia X Damage
Name:		xorg-lib-libXdamage
Version:	1.0.1
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXdamage-%{version}.tar.bz2
# Source0-md5:	4ba5a97a1dac93393290fe88b77f9641
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-proto-damageproto-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXdamage-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X Damage extension library.

%description -l pl
Biblioteka rozszerzenia X Damage.


%package devel
Summary:	Header files libXdamage development
Summary(pl):	Pliki nagłówkowe do biblioteki libXdamage
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXdamage = %{version}-%{release}
Requires:	xorg-proto-damageproto-devel
Requires:	xorg-lib-libXfixes-devel

%description devel
X Damage extension library.

This package contains the header files needed to develop programs that
use these libXdamage.

%description devel -l pl
Biblioteka rozszerzenia X Damage.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXdamage.


%package static
Summary:	Static libXdamage libraries
Summary(pl):	Biblioteki statyczne libXdamage
Group:		Development/Libraries
Requires:	xorg-lib-libXdamage-devel = %{version}-%{release}

%description static
X Damage extension library.

This package contains the static libXdamage library.

%description static -l pl
Biblioteka rozszerzenia X Damage.

Pakiet zawiera statyczną bibliotekę libXdamage.


%prep
%setup -q -n libXdamage-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXdamage.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXdamage.la
%attr(755,root,wheel) %{_libdir}/libXdamage.so
%{_pkgconfigdir}/xdamage.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXdamage.a
