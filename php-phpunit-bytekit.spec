%define		status		stable
%define		pearname	bytekit
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A command-line tool built on the PHP Bytekit extension
Name:		php-phpunit-bytekit
Version:	1.1.3
Release:	3
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	02c5a1a5cfe14ddb166ad8ed56bebcd5
URL:		http://github.com/sebastianbergmann/bytekit-cli
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(bytekit)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-ezc-ConsoleTools >= 1.6
Requires:	php-pear
Requires:	php-phpunit-File_Iterator >= 1.3.0
Requires:	php-symfony2-Finder >= 2.7.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Bytekit/Scanner/Rule/ZendView.php - not packaged anywhere yet
%define		_noautoreq_pear Symfony/Component/.* Bytekit/Scanner/Rule/ZendView.php

%description
A command-line tool built on the PHP Bytekit extension.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/bytekit
%{php_pear_dir}/Bytekit
