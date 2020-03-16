#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Diff-XS
Version  : 0.04
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Algorithm-Diff-XS-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Algorithm-Diff-XS-0.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-diff-xs-perl/libalgorithm-diff-xs-perl_0.04-5.debian.tar.xz
Summary  : Algorithm::Diff with XS core loop
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Algorithm-Diff-XS-license = %{version}-%{release}
Requires: perl-Algorithm-Diff-XS-perl = %{version}-%{release}
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
Provides: perl-Algorithm-Diff-XS-devel = %{version}-%{release}
Requires: perl-Algorithm-Diff-XS = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Diff-XS package.


%package license
Summary: license components for the perl-Algorithm-Diff-XS package.
Group: Default

%description license
license components for the perl-Algorithm-Diff-XS package.


%package perl
Summary: perl components for the perl-Algorithm-Diff-XS package.
Group: Default
Requires: perl-Algorithm-Diff-XS = %{version}-%{release}

%description perl
perl components for the perl-Algorithm-Diff-XS package.


%prep
%setup -q -n Algorithm-Diff-XS-0.04
cd %{_builddir}
tar xf %{_sourcedir}/libalgorithm-diff-xs-perl_0.04-5.debian.tar.xz
cd %{_builddir}/Algorithm-Diff-XS-0.04
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Algorithm-Diff-XS-0.04/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Diff-XS
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Diff-XS/49df8198b4a3807f63194671a3d2e74ae1fbd6ec
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
/usr/share/man/man3/Algorithm::Diff::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Diff-XS/49df8198b4a3807f63194671a3d2e74ae1fbd6ec

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Algorithm/Diff/XS.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/Algorithm/Diff/XS/XS.so
