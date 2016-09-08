Summary: Mosquitto Auth Plugin
Name: mosquitto-auth-plug
Version: 0.0.7
Release: 1
License: GPL
Group: System Environment/Base
Source: https://github.com/myDevicesIoT/Mosquitto-Auth-Plugin-RPM/blob/master/SOURCES/mosquitto-auth-plug-0.0.7.tar.gz
Requires: mosquitto

%description
Mosquitto Auth Plugin

%prep
%setup -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
%make_install

%clean
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/etc/mosquitto/auth-plug.so

%changelog
* Tue Sep 6 2016 David Achenbach <dachenbach@mydevices.com>
- RPM build directly from 0.0.7 source
