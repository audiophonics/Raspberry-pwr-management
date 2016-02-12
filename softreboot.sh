

!/bin/bash
PATH=/usr/bin:/home/pi/wiringPi/gpio
# Script to set GPIO 4 High and Reboot
echo "setting pin GPIO 4 High"
gpio -g mode 4 out
gpio -g write 4 1
sudo reboot
exit 0
