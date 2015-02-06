%define debug_package %{nil}
%define upstream_name    Syntax-Highlight-Engine-Kate
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    A Plugin for Component-Pascal syntax highlighting
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Syntax/Syntax-Highlight-Engine-Kate-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Syntax::Highlight::Engine::Kate is a port to perl of the syntax highlight
engine of the Kate text editor.

The language xml files of kate have been rewritten to perl modules using a
script. These modules function as plugins to this module.

Syntax::Highlight::Engine::Kate inherits
Syntax::Highlight::Engine::Kate::Template.

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
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 444023
- import perl-Syntax-Highlight-Engine-Kate


* Thu Sep 17 2009 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist

