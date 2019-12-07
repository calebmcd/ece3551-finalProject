import requests
import os
import json


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
    
def send_data(time,cal,fat,minHR,maxHR,avgHR):
     
     url='http://pi.calebmcd.com:1880/data'
     payload = {'time':time,'cal':cal,'fat':fat,'minHR':minHR,'maxHR':maxHR,'avgHR':avgHR}
     #payload = [time,cal,fat,minHR,maxHR,avgHR]
     
     r = requests.post(url, json=payload)
     print(r.status_code)


#.....
#.....
#.....


# time, cal, fat, minHR, maxHR, avgHR

send_data(5.3,123,78,62,167,122)
