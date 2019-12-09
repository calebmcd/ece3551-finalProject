from pulsesensor import Pulsesensor
import time
import RPi.GPIO as GPIO
import os
import requests
import pandas as pd
import pickle
from manageData import process

button = 23

toggle = False

a = ['BPM test']
a
['BPM test']

fileName = "BPMtest"

p = Pulsesensor()
p.startAsyncBPM()

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def swButton(ev=None):
    global toggle
    
    if toggle:
        print('Stopping Readings....')
        time.sleep(1)
        process()
    else:
        print('Starting Readings....')
    
    toggle = not toggle
    
def loop():
    global p
    global toggle
    
    if toggle:
        bpm = p.BPM

        file = open("workoutBPM.txt", 'w')
        #print('Button Pressed')
        if bpm > 0:
            print("BPM: %d" % bpm)
            file.write("hi")
            time.sleep(0.5)
        else:
            print("No Heartbeat found")
            time.sleep(1)

def destroy():
    p.stopAsyncBPM()
    GPIO.cleanup()
    file.close()
    
def send_data(time,cal,fat,minHR,maxHR,avgHR):
     
     url='http://pi.calebmcd.com:1880/data'
     payload = {'time':time,'cal':cal,'fat':fat,'minHR':minHR,'maxHR':maxHR,'avgHR':avgHR}
     #payload = [time,cal,fat,minHR,maxHR,avgHR]
     
     r = requests.post(url, json=payload)
     print(r.status_code)

if __name__ == '__main__':
    setup()
    GPIO.add_event_detect(button, GPIO.FALLING, callback=swButton, bouncetime=200)

while True:
    try:
        loop()
        time.sleep(0.5)
    except KeyboardInterrupt:
        destroy()