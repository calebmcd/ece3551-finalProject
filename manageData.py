import requests
import os
import json
import statistics
import pandas as pd
import pickle

#def store_data(dataSet):
#    data_to_send = {}
#    data_to_send['workout'] = []
#    data_to_send['workout'].append({
#        # time, cal, fat, minHR, maxHR, avgHR
#        'time': dataSet[0],
#        'cal': dataSet[1],
#        'fat': dataSet[2],
#        'minHR': dataSet[3],
#        'maxHR': dataSet[4],
#        'avgHR': dataSet[5]
#    })
#    
#    with open('calcData.txt', 'w') as outfile:
#        json.dump(data_to_send, outfile)
def saveData():
    

def calculate():
    print('Completing Calculations....')

def send_data(time,cal,fat,minHR,maxHR,avgHR):
     
     url='http://pi.calebmcd.com:1880/data'
     payload = {'time':time,'cal':cal,'fat':fat,'minHR':minHR,'maxHR':maxHR,'avgHR':avgHR}
     #payload = [time,cal,fat,minHR,maxHR,avgHR]
     
     r = requests.post(url, json=payload)
     print(r.status_code)

def process():
    print('Entered Processing')
    
#.....
#.....
#.....


# time, cal, fat, minHR, maxHR, avgHR

#send_data(23.8,1269,78,12,167,12)
