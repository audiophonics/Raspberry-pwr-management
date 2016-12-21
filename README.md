# Raspberry-pwr-management

## Installation of power button status on vanilla Raspbian

	sudo mkdir /usr/lib/audiophonics/
	sudo wget https://github.com/audiophonics/Raspberry-pwr-management/raw/master/runeaudio.sds.service -O /usr/lib/audiophonics/runeaudio.sds.service
	sudo wget https://github.com/audiophonics/Raspberry-pwr-management/raw/master/sds.sh -O /usr/lib/audiophonics/sds.sh

	sudo ln -s /usr/lib/audiophonics/runeaudio.sds.service /etc/systemd/system/runeaudio.sds.service
	sudo chmod +x /usr/lib/audiophonics/sds.sh
	sudo ln -s /usr/lib/audiophonics/sds.sh /usr/local/bin/sds.sh

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
