Summary:	X Damage extension library
Summary(pl):	Biblioteka rozszerzenia X Damage
Name:		xorg-lib-libXdamage
Version:	1.0.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/lib/libXdamage-%{version}.tar.bz2
# Source0-md5:	b0ab2a9e3d08896a40910246c8bcc335
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-proto-damageproto-devel >= 1.0
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXdamage
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Damage extension library.

%description -l pl
Biblioteka rozszerzenia X Damage.

%package devel
Summary:	Header files libXdamage development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXdamage
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-proto-damageproto-devel >= 1.0
Obsoletes:	libXdamage-devel

%description devel
X Damage extension library.

This package contains the header files needed to develop programs that
use these libXdamage.

%description devel -l pl
Biblioteka rozszerzenia X Damage.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXdamage.

%package static
Summary:	Static libXdamage library
Summary(pl):	Biblioteka statyczna libXdamage
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXdamage-static

%description static
X Damage extension library.

This package contains the static libXdamage library.

%description static -l pl
Biblioteka rozszerzenia X Damage.

Pakiet zawiera statyczn± bibliotekê libXdamage.

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
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXdamage.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXdamage.so
%{_libdir}/libXdamage.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xdamage.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXdamage.a
