%define upstream_name    Config-MVP
%define upstream_version 2.200003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Multivalue-property config-loading state machine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::OneArgNew)
BuildRequires:	perl(Role::HasMessage)
BuildRequires:	perl(Role::Identifiable::HasIdent)
BuildRequires:	perl(StackTrace::Auto)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.960
BuildRequires:	perl(Throwable)

Requires:	perl(Throwable)
Requires:	perl(Role::Identifiable::HasIdent)
Requires:	perl(Role::HasMessage)
Requires:	perl(StackTrace::Auto)
Requires:	perl(MooseX::OneArgNew)
BuildArch:	noarch

%description
MVP is a state machine for loading configuration (or other information) for
libraries. It expects to generate a list of named sections, each of which
relates to a Perl namespace and contains a set of named parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 2.200.1-2mdv2011.0
+ Revision: 653532
- add undetected requires

* Sat Feb 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.200.1-1
+ Revision: 640124
- new version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.101.650-2mdv2011.0
+ Revision: 555302
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.101.650-1mdv2011.0
+ Revision: 551990
- update to 2.101650

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.780-1mdv2010.1
+ Revision: 526435
- update to 0.100780

* Wed Dec 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.350-1mdv2010.1
+ Revision: 472580
- update to 0.093350

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.330-1mdv2010.1
+ Revision: 472239
- update to 0.093330

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.120-1mdv2010.1
+ Revision: 463097
- update to 0.093120

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.0-1mdv2010.1
+ Revision: 460712
- update to 0.093000

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.360-1mdv2010.0
+ Revision: 420856
- update to 0.092360

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.211-6mdv2010.0
+ Revision: 415035
- update to 0.092211

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.100-6mdv2010.0
+ Revision: 408648
- force rebuild
- update to 0.092100

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.60-1mdv2010.0
+ Revision: 400198
- update to 0.092060

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.40-1mdv2010.0
+ Revision: 399306
- import perl-Config-MVP


* Fri Jul 24 2009 cpan2dist 0.092040-1mdv
- initial mdv release, generated with cpan2dist
