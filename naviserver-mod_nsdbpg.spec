%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define packagename nsdbpg

Name:          naviserver-mod_nsdbpg
Summary:       NaviServer nsdbpg module
Version:       2.9
Release:       1
License:       MPL-2.0
Group:         Productivity/Networking/Web/Servers
Source:        %{packagename}.tar.gz
Patch0:        makefile.patch
URL:           https://sourceforge.net/projects/naviserver/
BuildRequires: make
BuildRequires: gcc
BuildRequires: postgresql-devel
BuildRequires: naviserver
BuildRequires: naviserver-devel
Requires:      tcl >= 8.6
Requires:      naviserver
BuildRoot:     %{buildroot}

%description
This module provides a straightforward database services driver for NaviServer.

%prep
%setup -q -n %{packagename}
%patch 0

%build
make 

%install
mkdir -p %{buildroot}/var/lib/naviserver/bin
make DESTDIR=%{buildroot} install

%clean
rm -rf %buildroot

%files
%dir %attr(-,nsadmin,nsadmin) /var/lib/naviserver
%defattr(-,nsadmin,nsadmin)
/var/lib/naviserver/bin/nsdbpg.so
