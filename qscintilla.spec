%include        /usr/lib/rpm/macros.python
Summary:	QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.
Summary(pl):	QScintilla jest portem do Qt dla edytora klas Neil'a Hodgson'a Scintilla C++.
Name:		qscintilla	
Version:	1.49
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.riverbankcomputing.co.uk/download/qscintilla/%{name}-%{version}-x11-gpl-0.3.tar.gz
URL:		http://www.riverbankcomputing.co.uk/qscintilla/index.php
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-x11-gpl-0.3-root-%(id -u -n)

%description
QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.

%description -l pl
QScintilla jest portem do Qt dla edytora klas Neil'a Hodgson'a Scintilla C++

%package devel
Summary:	Development files for the QScintilla
Summary(pl):	Pliki nag³ówkowe dla QScintilla
Group:          X11/Development/Libraries

%description devel
Contains the files necessary to develop applications using QScintilla - header
files

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki QScintilla

%prep
%setup -q -n %{name}-%{version}-x11-gpl-0.3

%build
QTDIR=%{_prefix}
export QTDIR
cd qt
qmake -o Makefile -after DESTDIR=tmp/ qscintilla.pro
#Potrzebna latka usuwajaca/przenoszaca z Makefile -  all: to co powinno znalezc sie w install:
%{__make}

cd ..
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/qt \
	$RPM_BUILD_ROOT%{_examplesdir}/qt/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/qt

cp qt/tmp/libqscintilla.so* $RPM_BUILD_ROOT%{_libdir}/qt
cp qt/qextscintilla*.h $RPM_BUILD_ROOT%{_includedir}/qt
cp qt/qscintilla*.qm $RPM_BUILD_ROOT%{_examplesdir}/qt/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog  NEWS  README doc/*
%attr(755,root,root) %{_libdir}

%files devel
%defattr(644,root,root,755)
%{_includedir}
%{_examplesdir}/qt/%{name}
