%define upstream_name    Config-MVP
%define upstream_version 2.200008

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Multivalue-property config-loading state machine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-MVP-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Class::Load) >= 0.170.0
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.300.0
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Module::Runtime)
BuildRequires: perl(Moose) >= 0.910.0
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::OneArgNew)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Role::HasMessage)
BuildRequires: perl(Role::Identifiable::HasIdent)
BuildRequires: perl(StackTrace::Auto)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More) >= 0.960.0
BuildRequires: perl(Throwable)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(namespace::autoclean)


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
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


