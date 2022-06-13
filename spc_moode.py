#!/usr/bin/python3
# Moode for Audiophonics SPC II power management board
# Initialisation of GPIO outputs 4 (SofthutDown) and 22 (BootOK) and 17 (Button shutdown)
# Script is lauched by /etc/rc.local
# Power LED stops slowly blinking and lights steadily after MoOde is ready
#
# All-in-One script 
# Start it without parameter to initialise
# "spc_moode.py reboot" to reboot
# "spc_moode.py shutdown" to shutdown


import sys
import os
import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

def boot():

    print ("Audiophonics initialisation script starting...")
    print ("Asserting pins : ")
    print ("SoftShutDown  : GPIO04=out, Low")
    print ("BootOK        : GPIO22=out, High")
    print ("Shutdown        : GPIO17=in")
 
    print ("Setting SoftShutDown output Low")
    GPIO.output(4,GPIO.LOW)
    print ("Setting BootOK output Low")
    GPIO.output(22,GPIO.LOW)

    
    # Testing Moode Ready :
    print ("Waiting for MoOde Availability")
    print ("Condition is checked out every 5 seconds")
    option= "-q"
    sqlSelect="select value from cfg_system where param='wrkready'"

    while True:
     result=subprocess.check_output(['/usr/local/bin/moodeutl',option,sqlSelect])
     if result == b'1\n':  #python3 binary value usage
     #if result[0] == "1": #python2 string value usage
       print ("Setting BootOK output High")
       GPIO.output(22,GPIO.HIGH)
       break
     time.sleep(2)

    # Button shutdown loop :
    while True :
        if GPIO.input(17) == 1: 
            print ("ShutDown order received, RaspBerry pi will now shutdown...")
            os.system ('sudo /usr/sbin/shutdown -h -P now')
            break
        time.sleep(2)
    sys.exit()

def shutdown():
    print ("RaspberryPi shutdown")
    print ("Setting pin GPIO4 High")
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    print ("Setting pin GPIO4 Low")
    GPIO.output(4,GPIO.LOW)
    time.sleep(1)
    os.system ('sudo shutdown -h -P now')
    sys.exit()

def reboot():
    print ("RaspberryPi Reboot")
    print ("Setting pin GPIO4 High")
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    os.system ('sudo reboot')
    sys.exit()

# Argument checking to know what to do :

if len(sys.argv) == 1 :
    boot()
elif sys.argv[1] == 'reboot':
    print ('Argument:', sys.argv[1])
    reboot()
elif sys.argv[1] == 'shutdown':
    print ('Argument:', sys.argv[1])
    shutdown()
else:
    print ("No valid argument, use nothing, reboot or shutdown")
    sys.exit()
