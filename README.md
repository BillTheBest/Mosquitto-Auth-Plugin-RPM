# Mosquitto-Auth-Plugin-RPM

This repo contains the files used to build am RPM of the auth plugin for the Mosquitto MQTT broker.

# Building a new RPM

```
ssh $BUILD_SERVER
cd /usr/src/rpm
# MAKE SURE THERE IS NOTHING TO SAVE HERE FIRST
sudo rm -rf *
sudo git clone git@github.com:myDevicesIoT/Mosquitto-Auth-Plugin-RPM.git
sudo rpmbuild -ba SPECS/mosquitto-auth-plug-0.0.7-1.spec
