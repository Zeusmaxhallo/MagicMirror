import subprocess
import time


import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

status = False


def set_display(x: bool):
    global status
    if x:
        subprocess.call("vcgencmd display_power 1", shell=True)
        status = True
        print("Display an!!!")
        print("sleeping 60 secs")
        for i in range(60,0):
            print("i")
            sleep(1)
    else:
        subprocess.call("vcgencmd display_power 0", shell=True)
        status = False
        print("Display aus")
        print("sleeping 10 secs")
        sleep(10)


while True:
    channel = GPIO.input(14)
    if channel:
        print("Bewegung!!!")
        if not status:
            set_display(True)
    else:
        if status:
            set_display(False)
    sleep(1)

