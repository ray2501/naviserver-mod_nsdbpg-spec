#!/usr/bin/tclsh

set arch "x86_64"
set base "naviserver-mod_nsdbpg-2.6"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force dbpg.h.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsdbpg.spec]
exec >@stdout 2>@stderr {*}$buildit
