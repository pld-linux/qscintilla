%include        /usr/lib/rpm/macros.python
Summary:	QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Summary(pl):	QScintilla jest portem do Qt klas C++ edytora Scintilla autorstwa Neila Hodgsona
Name:		qscintilla	
Version:	1.53
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://www.river-bank.demon.co.uk/download/QScintilla/%{name}-%{version}-x11-gpl-1.1.tar.gz
# Source0-md5:	1ad51e9e77a6b5213e7119b5ded56cf4
URL:		http://www.riverbankcomputing.co.uk/qscintilla/index.php
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-x11-gpl-0.3-root-%(id -u -n)

%description
QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.

%description -l pl
QScintilla jest portem do Qt klas C++ edytora Scintilla autorstwa
Neila Hodgsona.

%package devel
Summary:	Development files for the QScintilla
Summary(pl):	Pliki nag³ówkowe dla QScintilla
Group:		X11/Development/Libraries

%description devel
This package contains the header files necessary to develop
applications using QScintilla - header files.

%description devel -l pl
Pakiet tem zawiera pliki nag³ówkowe potrzebne do tworzenia i
kompilacji aplikacji korzystaj±cych z biblioteki QScintilla.

%prep
%setup -q -n %{name}-%{version}-x11-gpl-1.1

%build
QTDIR=%{_prefix}
export QTDIR
cd qt
qmake -o Makefile -after DESTDIR=tmp/ qscintilla.pro
#Potrzebna latka usuwajaca/przenoszaca z Makefile -  all: to co powinno znalezc sie w install:
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/qt \
	$RPM_BUILD_ROOT%{_examplesdir}/qt/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/qt

install qt/tmp/libqscintilla.so* $RPM_BUILD_ROOT%{_libdir}
install qt/qextscintilla*.h $RPM_BUILD_ROOT%{_includedir}/qt
install qt/qscintilla*.qm $RPM_BUILD_ROOT%{_examplesdir}/qt/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README doc/*
%attr(755,root,root) %{_libdir}/libqscintilla.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/qt/*.h
%{_examplesdir}/qt/%{name}
