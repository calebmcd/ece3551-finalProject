from pulsesensor import Pulsesensor
import time
import RPi.GPIO as GPIO
import requests
import pickle
import sys
import os
from manageData import process

button = 23
toggle = False
#url = 'http://pi.calebmcd.com:8000'
url = 'http://50.89.231.68:8000'

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
    global url
    
    if toggle:
        print('Stopping Readings....')
        
        tStop = time.perf_counter()
        totalTime = tStop-tStart
        
        timeFile = open('time','wb')
        newTime = pickle.dump(totalTime,timeFile)
        timeFile.close()
        
        requests.post(url + '/stop', json={ 'complete':True })
        time.sleep(1)
        process()
    else:
        print('Starting Readings....')
        requests.post(url + '/start', json={ 'complete':True })
        
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
    
    bpmPath = 'bpmFile.pickle'
    
    
    if toggle:
        bpm = p.BPM
        bpmArray = []
        
        #print('Button Pressed')
        if bpm > 0:
            
            # Load into array
            if os.path.exists(bpmPath):
                with open(bpmPath, 'rb') as ifi:
                    bpmArray = pickle.load(ifi)
                    
            print("BPM: %d" % bpm)
            
            # Append to array
            bpmArray.append(bpm)
            
            # Save array to Pickle file
            with open(bpmPath, 'wb') as ofi:
                pickle.dump(bpmArray, ofi)
            
            time.sleep(1)
        else:
            print("No Heartbeat found")
            time.sleep(1)

def destroy():
    p.stopAsyncBPM()
    GPIO.cleanup()
    sys.exit(0)
     

if __name__ == '__main__':
    setup()
    GPIO.add_event_detect(button, GPIO.FALLING, callback=swButton, bouncetime=1000)

while True:
    try:
        loop()
        time.sleep(0.5)
    except KeyboardInterrupt:
        destroy()