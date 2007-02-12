Summary:	Tool to enable KDE's KIOSK feature
Summary(pl.UTF-8):   Narzędzie do zarządzania możliwościami KIOSK w KDE
Name:		kiosktool
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/admin/%{name}-%{version}.tar.gz
# Source0-md5:	e23e4a52dfe09d03e8649364f91a818a
URL:		http://extragear.kde.org/apps/kiosktool/
BuildRequires:	expat-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Point&Click tool for system administrators to enable KDE's KIOSK
features or otherwise preconfigure KDE for groups of users.

%description -l pl.UTF-8
Narzędzie Wskaż i Kliknij dla administratorów do włączania możliwości
KIOSK w KDE i wstępnej konfiguracji grup użytkowników w KDE.

%prep
%setup -q

%build
%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiosktool
%attr(755,root,root) %{_bindir}/kiosktool-kdedirs
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/*/kiosktool.png
%{_desktopdir}/kde/*.desktop
