%define        _class           MDB2
%define        _subclass        Driver_mysql
%define        upstream_name    %{_class}_%{_subclass}

%define			beta b4

Name:           php-pear-%{upstream_name}
Version:        1.5.0b4
Release:        1
Summary:	Mysql MDB2 driver
License:        PHP License
Group:          Development/PHP
URL:            http://pear.php.net/package/MDB2_Driver_mysql/
Source0:        http://download.pear.php.net/package/MDB2_Driver_mysql-%{version}.tgz
Requires:       php-mysql
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-pear
BuildRequires:  php-pear
BuildArch:      noarch
Epoch:		1

%description
MDB2 MySQL driver.

%prep
%setup -q -c -n %{name}-%{version}%{beta}
mv package.xml %{upstream_name}-%{version}%{beta}/%{upstream_name}.xml

%install
%{__rm} -rf %{buildroot}

cd %{upstream_name}-%{version}%{beta}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b3.1mdv2011.0
+ Revision: 679278
- 1.5.0b3

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b2.3
+ Revision: 667573
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b2.2mdv2011.0
+ Revision: 607116
- rebuild

* Fri Mar 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b2.1mdv2010.1
+ Revision: 527660
- bump epoch
- 1.5.0b2
- fix versioning

* Thu Nov 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0b1-4mdv2010.1
+ Revision: 470289
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5.0b1-3mdv2010.0
+ Revision: 426653
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.0b1-2mdv2009.1
+ Revision: 321873
- rebuild

* Thu Oct 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.0b1-1mdv2009.1
+ Revision: 294353
- import php-pear-MDB2_Driver_mysql


* Thu Oct 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.0b1-1mdv2009.0
- initial Mandriva package


