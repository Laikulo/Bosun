# Bosun

## Goals
* Using a list of boards running klipper, and their connectivity methods and parameters, upgrade all to the same version with a minimum of human interaction.
* Provide a dbus service to allow control of the flashing process, list and manage available local versions, and download/request builds of binaries.

## Non-Goals
* Build klipper binaries, that is the goal of a related project. However, itegration with such a service is probably a good idea.
* Control klipper operation or machine state in general, maybe provide the service stop/start for klippy. (however, if a target needs an service restarted, like the linux_process version)
* Bosun should not explictly depend on using my fork of klipper, nor any other tools that are part of it's ecosystem (even though shipright, harbormaster and/or klipper-o-mat would probably be used in most installs)

## Ways to update boards
### Katapult over CAN
* verify klipper is not running
* request bootloader mode (flashtool -r)
* if a new canboot is scheduled, flash use canboot to flash the deployer, reboot if needed
* use katapult to flash ne binary

### Katapult over USB-CDC with CDC Klipper
* send the "request serial bootloader" magic klipper string
* flashtool -d /dev/DEVICE -f file.txt (katapult first if needed) 

### Katapult over USB-CDC with CanBridge
* request bootloader mode (flashtool -r)
* flashtool -d /dev/DEVICE (katapult first if needed)
