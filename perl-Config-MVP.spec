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
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Module::Pluggable::Object)

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
rm -fr t/basic.t

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


