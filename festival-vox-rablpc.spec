Summary:	British English male voice 'rab'
Summary(pl.UTF-8):	Brytyjska odmiana języka angielskiego - głos męski 'rab'
Name:		festival-vox-rablpc
Version:	0.1
Release:	3
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_rablpc16k.tar.gz
# Source0-md5:	cefcdda6cd48027da36d78f2f711451b
Requires:	festival-lex-OALD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides a British RP English male voice using a
residual excited LPC diphone synthesis method.  It uses a
modified Oxford Advanced Learners' Dictionary for pronunciations.
Prosodic phrasing is provided by a statistically trained model
using part of speech and local distribution of breaks.  Intonation
is provided by a CART tree predicting ToBI accents and an F0
contour generated from a model trained from natural speech. The
duration model is also trained from data using a CART tree.

%description -l pl.UTF-8
Ten pakiet udostępnia głos męski dla brytyjskiej odmiany języka
angielskiego. Używa wzbudzanej szczątkowo dwugłoskowej metody syntezy
LPC. Używa wymowy ze zmodyfikowanego słownika Oxford Advanced
Learners' Dictionary. Frazy prozodyczne są zapewnione przez
statystycznie nauczony model przy użyciu części mowy i lokalnego
rozłożenia przerw. Intonację zapewnia drzewo CART przewidujące akcenty
ToBI i obrys F0 generowany z modelu nauczonego na podstawie naturalnej
mowy. Model czasów trwania jest nauczony na podstawie danych z drzewa
CART.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english

cd festival/lib/voices/english
cp -r rab_diphone $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english
rm $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/rab_diphone/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/voices/english/rab_diphone/COPYING
%{_datadir}/festival/lib/voices/english/rab_diphone
