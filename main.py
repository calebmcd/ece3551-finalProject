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

p = Pulsesensor()
p.startAsyncBPM()

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def swButton(ev=None):
    global toggle
    global tStart
    global tStop
    global totalTime
    
    if toggle:
        print('Stopping Readings....')
        
        tStop = time.perf_counter()
        totalTime = tStop-tStart
        
        timeFile = open('time','wb')
        newTime = pickle.dump(totalTime,timeFile)
        timeFile.close()
        
        #destroy()
        time.sleep(1)
        process()
    else:
        print('Starting Readings....')
        tStart = time.perf_counter()
    
    toggle = not toggle
    

    
#def read():
    #readFile = open('allBPM', 'rb')
    #new_dict = pickle.load(readFile)
    #readFile.close()
    #print(new_dict)
    
    
def loop():
    global p
    global toggle
    global bpmFile
    
    if toggle:
        bpm = p.BPM
        
        #print('Button Pressed')
        if bpm > 0:
            bpmFile = open('allBPM','wb')
            print("BPM: %d" % bpm)
            #strBPM = str(bpm)
            pickle.dump(bpm, bpmFile)
            time.sleep(1)
        else:
            print("No Heartbeat found")
            time.sleep(1)

def destroy():
    p.stopAsyncBPM()
    GPIO.cleanup()
     

if __name__ == '__main__':
    setup()
    GPIO.add_event_detect(button, GPIO.FALLING, callback=swButton, bouncetime=200)

while True:
    try:
        loop()
        time.sleep(0.5)
    except KeyboardInterrupt:
        destroy()