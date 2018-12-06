#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Diff-XS
Version  : 0.04
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Algorithm-Diff-XS-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Algorithm-Diff-XS-0.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-diff-xs-perl/libalgorithm-diff-xs-perl_0.04-5.debian.tar.xz
Summary  : Algorithm::Diff with XS core loop
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Algorithm-Diff-XS-lib = %{version}-%{release}
Requires: perl-Algorithm-Diff-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::Diff)

%description
NAME
Algorithm::Diff::XS - Algorithm::Diff with XS core loop
SYNOPSIS
# Drop-in replacement to Algorithm::Diff, but "compact_diff"
# and C<LCSidx> will run much faster for large data sets.
use Algorithm::Diff::XS qw( compact_diff LCSidx );

%package dev
Summary: dev components for the perl-Algorithm-Diff-XS package.
Group: Development
Requires: perl-Algorithm-Diff-XS-lib = %{version}-%{release}
Provides: perl-Algorithm-Diff-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Diff-XS package.


%package lib
Summary: lib components for the perl-Algorithm-Diff-XS package.
Group: Libraries
Requires: perl-Algorithm-Diff-XS-license = %{version}-%{release}

%description lib
lib components for the perl-Algorithm-Diff-XS package.


%package license
Summary: license components for the perl-Algorithm-Diff-XS package.
Group: Default

%description license
license components for the perl-Algorithm-Diff-XS package.


%prep
%setup -q -n Algorithm-Diff-XS-0.04
cd ..
%setup -q -T -D -n Algorithm-Diff-XS-0.04 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Algorithm-Diff-XS-0.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Diff-XS
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Diff-XS/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Algorithm/Diff/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Diff::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Algorithm/Diff/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Diff-XS/deblicense_copyright
