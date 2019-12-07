from pulsesensor import Pulsesensor
import time
import RPi.GPIO as GPIO
import os
import requests

button = 23

latestState = 0

p = Pulsesensor()
p.startAsyncBPM()

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def swButton(ev=None):
    global latestState
    global p
    
    bpm = p.BPM
    
    latestState = not latestState
    
    while (latestState):
        file = open("workoutBPM.txt", 'w')
        #print('Button Pressed')
        if bpm > 0:
            print("BPM: %d" % bpm)
            file.write("hi")
            time.sleep(1)
        else:
            print("No Heartbeat found")

def loop():
    GPIO.add_event_detect(button, GPIO.FALLING, callback=swButton, bouncetime=200)
    while True:
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
    try:
        loop()
    except KeyboardInterrupt:
        destroy()