Summary:	Sc is a free curses-based spreadsheet program that uses key bindings similar to vi and less
Summary(pl.UTF-8):	Sc jest darmowym, bazującym na curses arkuszem kalkulacyjnym, uzywającym skrótów klawiszowych podobnych do vi oraz less
Name:		sc
Version:	7.16
Release:	4
License:	Public Domain
Group:		Applications/Math
Source0:	http://www.ibiblio.org/pub/Linux/apps/financial/spreadsheet/%{name}-%{version}.tar.gz
# Source0-md5:	1db636e9b2dc7cd73c40aeece6852d47
# https://launchpad.net/ubuntu/hoary/+source/sc/7.16-2/+files/sc_7.16-2.diff.gz
Patch0:		%{name}_%{version}-2.diff
URL:		http://www.ibiblio.org/pub/Linux/apps/financial/spreadsheet/
BuildRequires:	bison
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sc is a spreadsheet calculator based on rectangular tables like a
financial spreadsheet. When invoked it presents you with a table
organized as rows and columns of cells. If invoked without a file
argument, by default the initial table is empty. Each cell can be
associated with a numeric value, a label string and/or an expression
which evaluates to a numeric value or label string, often based on
other cell values (formula).

%description -l pl.UTF-8
Sc jest jest arkuszem kalkulacyjnym bazującym na prostokątnych
tabelkach, takich jak finansowe arkusze. Po odpaleniu zaprezentuje
tabelke zorganizowaną z wierszy i kolumn komórek. Jeżeli zostanie
wywołany bez argumentu plikowego, domyślnie tabelka będzie pusta.
Każdej komórce można przypisać wartość numeryczną, tekstową etykietę
oraz/lub wyrażenie rozwijane do wartości numerycznej lub etykiety
tesktowej, często bazując na wartościach innych komórek (formuła).

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -I/usr/include/ncurses -DSYSV3" \
	LIBDIR="%{_libdir}/sc"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/sc,%{_mandir}/man1}
%{__make} prefix="$RPM_BUILD_ROOT%{_prefix}" \
	LIBDIR="$RPM_BUILD_ROOT%{_libdir}/sc" \
	MANDIR="$RPM_BUILD_ROOT%{_mandir}/man1" \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README VMS_NOTES SC.MACROS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/sc
%dir %{_libdir}/sc/plugins
%{_libdir}/sc/tutorial.sc
%{_mandir}/man1/*
