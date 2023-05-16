# Raspberry-pwr-management

New experimental version to have the softshutdown and softreboot working properly in bullseye based distributions. 
Currently working and tested on moodeAudio.


## Requirements
* This software uses gpioset from *gpiod*. The installation procedure will automatically try to install this dependency using apt-get.
* Systemd (debian flavor) is required since the whole system uses ```/lib/systemd/system-shutdown/```
* Kernel Linux Raspberry Pi 3.18 & above

## How to install

```shell 
cd ~
wget https://github.com/audiophonics/Raspberry-pwr-management/archive/moode_dev.tar.gz 
tar -xzf moode_dev.tar.gz 
cd "Raspberry-pwr-management-moode_dev"
sudo sh pispcii install moode                                                                
cd ~
rm -f moode_dev.tar.gz
sudo reboot

```

## What does it do 
### config.txt
Its installation process adds the following to /boot/config.txt in order to have the kernel handling basic bootOK / safe shutdown button working.
```
dtoverlay=gpio-poweroff,gpiopin=22,active_low
dtoverlay=gpio-shutdown,gpio_pin=17,active_low=0,gpio_pull=down
``` 

### Systemd
The file also links itself to */lib/systemd/system-shutdown/* and triggers the corresponding GPIO in response to shutdown / reboot events.


### GPIO reservation
Using this software will use the GPIO pins 
* 4 
* 17
* 22

*Please make sure none of them are used by any other process.*



## TESTED ON 
* moodeAudio 8.3.2 64bit (Rasptouch)
* moodeAudio 8.3.2 32bit (Rasptouch)
