%define		_modname	openal
%define		_status		beta
Summary:	%{_modname} - bindings to OpenAL
Summary(pl):	%{_modname} - dowi±zania do OpenAL
Name:		php-pecl-%{_modname}
Version:	0.1
Release:	0.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	d6dd7f9d47997928e6d897cb711317ba
URL:		http://pecl.php.net/package/openal/
BuildRequires:	OpenAL-devel
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension provides platform independent sound bindings.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie dostarcza niezale¿nych od platformy dowi±zañ dotycz±cych
d¼wiêku.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
