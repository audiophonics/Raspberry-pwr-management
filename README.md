# Raspberry-pwr-management

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
	
