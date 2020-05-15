#AUDIOPHONICS SPC POWER CONTROLLER
#Python RPI-GPIO Script
#In case WiringPi do not work
#Python, PIP and RPI.GPIO must be installed
#(pip install RPi.GPIO)
#Must be run as root to be able to send shutdown order

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!")
GPIO.setmode(GPIO.BCM)
import time
import os


#Set GPIO used here :
bootok = 22
shutdown = 17

print 'Audiophonics Shutdown script starting...'
print "Asserting pins : "
print "BootOK   : GPIO"+str(bootok)+"=out, High"
print "ShutDown : GPIO"+str(shutdown)+"=in, Low"

#When script Launched, send BOOT OK signal

GPIO.setup(bootok, GPIO.OUT)
GPIO.output(bootok, GPIO.HIGH)

# Initialise GPIO 17 for shutdown order
GPIO.setup(shutdown, GPIO.IN)


while True :
	sdstate = GPIO.input(shutdown)
	#print sdstate
	time.sleep(0.5)
	if sdstate == 1 :
		print "ShutDown order received, RaspBerry pi will now shutdown..."
		time.sleep(0.5)
		os.system('shutdown -h -P now')
		break
