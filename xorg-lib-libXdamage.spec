Summary:	X Damage extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Damage
Name:		xorg-lib-libXdamage
Version:	1.1.6
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXdamage-%{version}.tar.xz
# Source0-md5:	ca55d29fa0a8b5c4a89f609a7952ebf8
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
BuildRequires:	xorg-proto-fixesproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	libXdamage < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Damage extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Damage.

%package devel
Summary:	Header files for libXdamage library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXdamage
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-proto-damageproto-devel >= 1.1
Obsoletes:	libXdamage-devel < 1.1

%description devel
X Damage extension library.

This package contains the header files needed to develop programs that
use libXdamage.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Damage.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXdamage.

%package static
Summary:	Static libXdamage library
Summary(pl.UTF-8):	Biblioteka statyczna libXdamage
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXdamage-static < 1.1

%description static
X Damage extension library.

This package contains the static libXdamage library.

%description static -l pl.UTF-8
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXdamage.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libXdamage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXdamage.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXdamage.so
%{_includedir}/X11/extensions/Xdamage.h
%{_pkgconfigdir}/xdamage.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXdamage.a
