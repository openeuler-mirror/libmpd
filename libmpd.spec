Name:           libmpd
Version:        11.8.17
Release:        2
Summary:        Music Player Daemon Library
Group:          Development/Libraries
License:        GPLv2+
URL:            http://gmpc.wikia.com/wiki/Gnome_Music_Player_Client
Source:         http://download.sarine.nl/Programs/gmpc/11.8/libmpd-11.8.17.tar.gz
Patch0:         libmpd-11.8.17-strndup.patch
BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.16
%description
libmpd is an abstraction around libmpdclient. It provides an easy and reliable callback based interface to mpd.

%package devel
Requires: %{name} = %{version}
Requires: pkgconfig

Summary:        Development files for %{name}
%description devel
libmpd-devel contains libraries and header files for developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .strndup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR="$RPM_BUILD_ROOT" install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%doc ChangeLog COPYING README
%{_libdir}/libmpd.so.1*

%files devel
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd-1.0

%changelog
* Wed Jul 8 2020 Dillon Chen <dillon.chen@turbolinux.com.cn> - 11.8.17-1
- Init Package
- history 0.20.0, next 11.8.17
