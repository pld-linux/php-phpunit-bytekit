%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	bytekit
Summary:	%{pearname} - A command-line tool built on the PHP Bytekit extension
Name:		php-phpunit-bytekit
Version:	1.1.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	dec667472af72b36c7fd3dcfe7c43364
URL:		http://github.com/sebastianbergmann/bytekit-cli
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.8.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-bytekit
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-File_Iterator >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
