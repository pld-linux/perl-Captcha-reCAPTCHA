#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Captcha
%define	pnam	reCAPTCHA
Summary:	Captcha::reCAPTCHA - A Perl implementation of the reCAPTCHA API
#Summary(pl.UTF-8):	
Name:		perl-Captcha-reCAPTCHA
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AN/ANDYA/Captcha-reCAPTCHA-%{version}.tar.gz
# Source0-md5:	1b4bf7d20d720ff7ac8622f40d63139e
URL:		http://search.cpan.org/dist/Captcha-reCAPTCHA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTML::Tiny) >= 0.904
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
reCAPTCHA is a hybrid mechanical turk and captcha that allows visitors
who complete the captcha to assist in the digitization of books.

See http://recaptcha.net/learnmore.html.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Captcha
%{perl_vendorlib}/Captcha/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
