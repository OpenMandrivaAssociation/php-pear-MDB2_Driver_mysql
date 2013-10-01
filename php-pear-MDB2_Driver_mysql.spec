%define _class           MDB2
%define _subclass        Driver_mysql
%define modname    %{_class}_%{_subclass}
%define beta b4

Summary:	Mysql MDB2 driver
Name:		php-pear-%{modname}
Epoch:		1
Version:	1.5.0
Release:	0.0.%{beta}
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/MDB2_Driver_mysql/
Source0:	http://download.pear.php.net/package/MDB2_Driver_mysql-%{version}%{beta}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires:	php-mysql
Requires(post,preun):	php-pear
Requires:	php-pear

%description
MDB2 MySQL driver.

%prep
%setup -qc -n %{name}-%{version}%{beta}
mv package.xml %{modname}-%{version}%{beta}/%{modname}.xml

%install
cd %{modname}-%{version}%{beta}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

