Summary:	QScintilla - a port of Neil Hodgson's Scintilla C++ editor class to Qt
Summary(pl):	QScintilla - port do Qt klas C++ edytora Scintilla autorstwa Neila Hodgsona
Name:		qscintilla
Version:	1.2
%define	scintilla_ver	1.54
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.river-bank.demon.co.uk/download/QScintilla/%{name}-%{scintilla_ver}-x11-gpl-%{version}.tar.gz
# Source0-md5:	a69bf732c40df24c1e57d152cbf25729
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
Requires:	%{name} = %{epoch}:%{version}
Requires:	qt-devel

%description devel
This package contains the header files necessary to develop
applications using QScintilla - header files.

%description devel -l pl
Pakiet tem zawiera pliki nag³ówkowe potrzebne do tworzenia i
kompilacji aplikacji korzystaj±cych z biblioteki QScintilla.

%prep
%setup -q -n %{name}-%{scintilla_ver}-x11-gpl-%{version}

%build
QTDIR=%{_prefix}
export QTDIR
cd qt
qmake -o Makefile -after DESTDIR=tmp qscintilla.pro
#Potrzebna latka usuwajaca/przenoszaca z Makefile -  all: to co powinno znalezc sie w install:
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/qt \
	$RPM_BUILD_ROOT%{_examplesdir}/qt/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/qt \
	$RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES
	
cp -df qt/tmp/libqscintilla.so* $RPM_BUILD_ROOT%{_libdir}
install qt/qextscintilla*.h $RPM_BUILD_ROOT%{_includedir}/qt

# where should it be placed to be used?
# README says $QTDIR/translations, but it doesn't exist
install qt/qscintilla_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/qscintilla.qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libqscintilla.so.*.*.*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qscintilla.qm

%files devel
%doc doc/*
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqscintilla.so
%{_includedir}/qt/*.h
