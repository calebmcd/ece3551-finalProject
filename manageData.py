import requests
import os
import json
import statistics
import pandas as pd
import pickle

def pullData():
    
    global userData
    
    url = 'http://192.168.50.13:8000/pulldata'
    
    userData = (requests.get(url)).json()
    
    
def calculate():
    global userData
    
    pullData()
    
    print('Completing Calculations....')
    readFile = open('allBPM', 'rb')
    new_dict = pickle.load(readFile)
    readFile.close()
    
    readTimeFile = open('time', 'rb')
    timeDict = pickle.load(readTimeFile)
    readTimeFile.close()
    
    #readUserData = open('userSettings', 'rb')
    #UserData = pd.read_pickle(
    
    age = userData['age']
    weight = userData['weight']
    
    time = (timeDict/60)
    avgHR = new_dict
    
    calBurnedMale = ((age*0.2017)+(avgHR*0.6309)-(weight*0.09036)-55.0969)*(timeDict/4.184)
    fatBurnedMale = (calBurnedMale/3500)
    
    calBurnedFemale =((age*0.074)+(avgHR*0.4472)-(weight*0.05741)-20.4022)*(timeDict/4.184)
    fatBurnedFemale = (calBurnedFemale/3500)
    
    print("You burned ", round(calBurnedMale, 5), " calories and ", round(fatBurnedMale, 5), " pounds")
    print("You worked out for ",round(time,2)," minutes.")
    print("Your average heart rate was ", round(avgHR, 4))
    
    os.remove('time')
    os.remove('allBPM')
    
    Stats = [round(time,2),round(calBurnedMale,4),round(fatBurnedMale,4),round(calBurnedFemale,4),round(fatBurnedFemale,4),round(avgHR,4)]
    return Stats
    

def send_data(statArray):
    
    global userData
    
    url = 'http://192.168.50.13:8000/data'
    payload = {'time':statArray[0],'calMale':statArray[1],'fatMale':statArray[2],'calFemale':statArray[3],'fatFemale':statArray[4],'avgHR':statArray[5],'gender':userData['gender']}
     
    requests.post(url, json=payload)

def process():
    print('Calculating Data.....')
    data_to_send = calculate()
    print('Sending Data to Server.....')
    send_data(data_to_send)
    print('Data Sent!')
