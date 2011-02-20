%define upstream_name    Config-MVP
%define upstream_version 2.200001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Multivalue-property config-loading state machine
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(MooseX::OneArgNew)
BuildRequires: perl(Role::HasMessage)
BuildRequires: perl(Role::Identifiable::HasIdent)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
MVP is a state machine for loading configuration (or other information) for
libraries. It expects to generate a list of named sections, each of which
relates to a Perl namespace and contains a set of named parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
