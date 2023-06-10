#
# Conditional build:
%bcond_without	dmx		# DMX support (xserver < 21)
%bcond_with	xf86misc	# XF86-Misc extensions support (xserver < 1.6)

Summary:	xdpyinfo application - display information utility for X
Summary(pl.UTF-8):	Aplikacja xdpyinfo - narzędzie do wyświetlania informacji dla X
Name:		xorg-app-xdpyinfo
Version:	1.3.4
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xdpyinfo-%{version}.tar.xz
# Source0-md5:	933e6d65f96c890f8e96a9f21094f0de
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
%{?with_xf86misc:BuildRequires:	xorg-lib-libXxf86misc-devel}
BuildRequires:	xorg-lib-libXxf86vm-devel
%{?with_dmx:BuildRequires:	xorg-lib-libdmx-devel}
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
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
%configure \
	%{?with_dmx:--with-dmx} \
	%{?with_xf86misc:--with-xf86misc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.1*
