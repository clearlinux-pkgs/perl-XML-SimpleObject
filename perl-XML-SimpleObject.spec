#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-SimpleObject
Version  : 0.53
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/D/DB/DBRIAN/XML-SimpleObject-0.53.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DB/DBRIAN/XML-SimpleObject-0.53.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-simpleobject-perl/libxml-simpleobject-perl_0.53-3.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-XML-SimpleObject-license = %{version}-%{release}
Requires: perl-XML-SimpleObject-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::LibXML)
BuildRequires : perl(XML::Parser)
BuildRequires : perl(XML::SAX::Exception)

%description
==================================================================
XML::SimpleObject

%package dev
Summary: dev components for the perl-XML-SimpleObject package.
Group: Development
Provides: perl-XML-SimpleObject-devel = %{version}-%{release}
Requires: perl-XML-SimpleObject = %{version}-%{release}

%description dev
dev components for the perl-XML-SimpleObject package.


%package license
Summary: license components for the perl-XML-SimpleObject package.
Group: Default

%description license
license components for the perl-XML-SimpleObject package.


%package perl
Summary: perl components for the perl-XML-SimpleObject package.
Group: Default
Requires: perl-XML-SimpleObject = %{version}-%{release}

%description perl
perl components for the perl-XML-SimpleObject package.


%prep
%setup -q -n XML-SimpleObject0.53
cd %{_builddir}
tar xf %{_sourcedir}/libxml-simpleobject-perl_0.53-3.debian.tar.xz
cd %{_builddir}/XML-SimpleObject0.53
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-SimpleObject0.53/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-SimpleObject
cp %{_builddir}/XML-SimpleObject0.53/deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-SimpleObject/1ff5ce591a7a312c1cac9973ab0b14d6cb1db067
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::SimpleObject.3
/usr/share/man/man3/XML::SimpleObject::LibXML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-SimpleObject/1ff5ce591a7a312c1cac9973ab0b14d6cb1db067

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/XML/SimpleObject.pm
/usr/lib/perl5/vendor_perl/5.30.1/XML/SimpleObject/Enhanced.pm
/usr/lib/perl5/vendor_perl/5.30.1/XML/SimpleObject/LibXML.pm
/usr/lib/perl5/vendor_perl/5.30.1/XML/SimpleObject/ex.pl
/usr/lib/perl5/vendor_perl/5.30.1/XML/ex.pl
