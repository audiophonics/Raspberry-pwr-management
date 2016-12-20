#!/bin/bash
# Audiophonics
# Shutdown detection script
# Script to set GPIO 4 High for 1sec

PATH=/usr/bin:/home/pi/wiringPi/gpio

# Script to set GPIO 4 High and Reboot
# Reboot blink will stop after Boot OK return
echo "setting pin GPIO 4 High"
gpio -g mode 4 out
gpio -g write 4 1
echo "Raspberry Pi Reboot"
sudo reboot
exit 0
