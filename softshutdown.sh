#!/bin/bash
# Audiophonics
# Shutdown detection script
# Script to set GPIO 4 High for 1sec

PATH=/usr/bin:/home/pi/wiringPi/gpio

echo "Setting pin GPIO4 High"
gpio mode 7 out
gpio write 7 1
sleep 1
echo "Setting pin GPIO4 Low"
gpio write 7 0

echo "RaspberryPi shutdown"
sudo shutdown -h -P now
exit 0
