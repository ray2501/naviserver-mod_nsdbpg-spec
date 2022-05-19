#
# spec file for package naviserver nsdbpg module
#

Summary:        NaviServer nsdbpg module
Name:           naviserver-mod_nsdbpg
Version:        2.6
Release:        1
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsdbpg
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
BuildRequires:  postgresql-devel
Requires:       naviserver
Source0:        %{name}-%{version}.tar.gz
Patch0:         dbpg.h.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This module implements a simple NaviServer/AOLserver database services driver.
The driver is for the PostgreSQL ORDBMS.

%prep
%setup -q %{name}-%{version}
%patch0

%build
make NAVISERVER=/var/lib/naviserver

%install
mkdir -p %buildroot/var/lib/naviserver/bin
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%post -n naviserver-mod_nsdbpg
/sbin/ldconfig

%postun -n naviserver-mod_nsdbpg
/sbin/ldconfig

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/bin/nsdbpg.so

%changelog

