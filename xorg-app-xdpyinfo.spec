Summary:	xdpyinfo application - display information utility for X
Summary(pl.UTF-8):	Aplikacja xdpyinfo - narzędzie do wyświetlania informacji dla X
Name:		xorg-app-xdpyinfo
Version:	1.3.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xdpyinfo-%{version}.tar.bz2
# Source0-md5:	8809037bd48599af55dad81c508b6b39
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libdmx-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdpyinfo is a utility for displaying information about an X server.

It is used to examine the capabilities of a server, the predefined
values for various parameters used in communicating between clients
and the server, and the different types of screens, visuals, and X11
protocol extensions that are available.

%description -l pl.UTF-8
xdpyinfo to narzędzie do wyświetlania informacji o serwerze X.

Służy do sprawdzania możliwości serwera, predefiniowanych wartości
różnych parametrów używanych w komunikacji między klientami a serwerem
oraz dostępności różnych rodzajów ekranów, widoków i rozszerzeń
protokołu X11.

%prep
%setup -q -n xdpyinfo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.1*
