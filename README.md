# Raspberry-pwr-management

## Standard pins are :
- Boot OK : GPIO 22
- Shutdown : GPIO 17
- SoftShutdown : GPIO 4

Allo Digione is using GPIO17, so sds.sh must be modified if using this HAT board. (e.g. 27)

## Using the SPC board with standard RPI power management overlays :

Edit /boot/config.txt, add :
```
dtoverlay=gpio-poweroff,gpiopin=22,active_low
dtoverlay=gpio-shutdown,gpio_pin=17,active_low=0,gpio_pull=down
```
That's all, you will be able to control power of the RPI with SPC, having a real power shutdown, and no CPU idle.
Compatible with most *if not all* distributions.
However the power will not be cut if you initiate Power Off from software, only from button, this behavior require a script.

## Installation on Moode Audio

	cd /home/pi
	wget https://raw.githubusercontent.com/audiophonics/Raspberry-pwr-management/master/sds_moode.sh
	wget https://raw.githubusercontent.com/audiophonics/Raspberry-pwr-management/master/softshutdown_moode.sh
	mv sds_moode.sh sds.sh
	mv softshutdown_moode.sh softshutdown.sh
	sudo chmod +x sds.sh
	sudo chmod +x softshutdown.sh
	
	cd /var/local/www/commandw/
	sudo nano restart.sh

- Update this section :
```
	if [[ $1 = "poweroff" ]]; then
	mpc stop
	systemctl stop nginx
	/home/pi/softshutdown.sh
	#      poweroff
	fi
```

- Edit rc.local :

```
	sudo nano /etc/rc.local
	
	Add before exit : 
	sudo bash /home/pi/sds.sh &
```


## Installation of power button status on vanilla Raspbian

	sudo mkdir /usr/lib/audiophonics/
	sudo wget https://github.com/audiophonics/Raspberry-pwr-management/raw/master/runeaudio.sds.service -O /usr/lib/audiophonics/runeaudio.sds.service
	sudo wget https://github.com/audiophonics/Raspberry-pwr-management/raw/master/sds.sh -O /usr/lib/audiophonics/sds.sh

	sudo ln -s /usr/lib/audiophonics/runeaudio.sds.service /etc/systemd/system/runeaudio.sds.service
	sudo chmod +x /usr/lib/audiophonics/sds.sh
	sudo ln -s /usr/lib/audiophonics/sds.sh /usr/local/bin/sds.sh
	
	sudo systemctl enable runeaudio.sds.service 
	sudo systemctl start runeaudio.sds.service

## Installation of soft reboot on vanilla Raspbian

	sudo mkdir /usr/lib/audiophonics/
	sudo wget https://github.com/audiophonics/Raspberry-pwr-management/raw/master/softreboot.sh -O /usr/lib/audiophonics/softreboot.sh
	sudo chmod +x /usr/lib/audiophonics/softreboot.sh
	sudo ln -s /usr/lib/audiophonics/softreboot.sh /usr/bin/softreboot.sh

## Installation of soft shutdown on vanilla Raspbian

	sudo mkdir /usr/lib/audiophonics/
	sudo wget https://github.com/audiophonics/Raspberry-pwr-management/raw/master/softshutdown.sh -O /usr/lib/audiophonics/softshutdown.sh
	sudo chmod +x /usr/lib/audiophonics/softshutdown.sh
	sudo ln -s /usr/lib/audiophonics/softshutdown.sh /usr/bin/softshutdown.sh

## Installation on Volumio 2

	Instructions on our Forum
	http://forum.audiophonics.fr/viewtopic.php?f=12&t=1967&p=7991


## Volumio 2 Plugin from Saiyato

	Thanks to him for this very nice plugin
	https://github.com/Saiyato/volumio-audiophonicsonoff-plugin
	
	Installation :
	mkdir ./audiophonicsonoff-plugin
	wget https://github.com/Saiyato/volumio-audiophonicsonoff-plugin/raw/master/volumio-audiophonicsonoff-plugin.zip
	miniunzip volumio-audiophonicsonoff-plugin.zip -d ./audiophonicsonoff-plugin
	cd ./audiophonicsonoff-plugin
	/// From Volumio 2.457 :
	apt-get update && apt-get install -y build-essential
	npm i
	From Volumio 2.457  \\\
	volumio plugin install
	
