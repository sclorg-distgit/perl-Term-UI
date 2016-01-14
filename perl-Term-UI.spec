%{?scl:%scl_package perl-Term-UI}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Term-UI
Version:        0.38
Release:        2%{?dist}
Summary:        Term::ReadLine user interface made easy
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Term-UI/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Term-UI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  %{?scl_prefix}perl(deprecate)
%endif
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Log::Message)
BuildRequires:  %{?scl_prefix}perl(Log::Message::Simple)
BuildRequires:  %{?scl_prefix}perl(Params::Check)
BuildRequires:  %{?scl_prefix}perl(Term::ReadLine)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
%if 0%(perl -e 'print $] > 5.017')
Requires:       %{?scl_prefix}perl(deprecate)
%endif

%description
Term::UI is a transparent way of eliminating the overhead of having to
format a question and then validate the reply, informing the user if the
answer was not proper and re-issuing the question.

%prep
%setup -q -n Term-UI-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Rebuilt with newer perl516-build
- Resolves: rhbz#1040474

* Wed Nov 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- 0.38 bump

* Mon Feb 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-1
- SCL package - initial import
