# TODO: Consider renaming to QScintilla1 ?
%define	scintilla_ver	1.71
Summary:	QScintilla - a port of Neil Hodgson's Scintilla C++ editor class to Qt
Summary(pl.UTF-8):	QScintilla - port do Qt klas C++ edytora Scintilla autorstwa Neila Hodgsona
Name:		qscintilla
Version:	1.7.1
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://www.riverbankcomputing.com/Downloads/QScintilla1/QScintilla-%{scintilla_ver}-gpl-%{version}.tar.gz
# Source0-md5:	dfa047b45d4f09ae8d4a8a431ba88a5a
URL:		http://www.riverbankcomputing.co.uk/qscintilla/index.php
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	scintilla-devel >= %{scintilla_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.

%description -l pl.UTF-8
QScintilla jest portem do Qt klas C++ edytora Scintilla autorstwa
Neila Hodgsona.

%package devel
Summary:	Development files for the QScintilla
Summary(pl.UTF-8):	Pliki nagłówkowe dla QScintilla
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	qt-devel

%description devel
This package contains the header files necessary to develop
applications using QScintilla - header files.

%description devel -l pl.UTF-8
Pakiet tem zawiera pliki nagłówkowe potrzebne do tworzenia i
kompilacji aplikacji korzystających z biblioteki QScintilla.

%prep
%setup -q -n QScintilla-%{scintilla_ver}-gpl-%{version}

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
	$RPM_BUILD_ROOT%{_datadir}/locale/{de,fr,pt_BR,ru}/LC_MESSAGES

cp -df qt/tmp/libqscintilla.so* $RPM_BUILD_ROOT%{_libdir}
install qt/qextscintilla*.h $RPM_BUILD_ROOT%{_includedir}/qt

# where should it be placed to be used?
# README says $QTDIR/translations, but it doesn't exist
install qt/qscintilla_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/qscintilla.qm
install qt/qscintilla_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/qscintilla.qm
install qt/qscintilla_ru.qm $RPM_BUILD_ROOT%{_datadir}/locale/ru/LC_MESSAGES/qscintilla.qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libqscintilla.so.*.*.*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qscintilla.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qscintilla.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/qscintilla.qm

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libqscintilla.so
%{_includedir}/qt/*.h
