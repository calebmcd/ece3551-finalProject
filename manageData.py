import requests
import os
import json

def store_data(dataSet):
    data_to_send = {}
    data_to_send['workout'] = []
    data_to_send['workout'].append({
        # time, cal, fat, minHR, maxHR, avgHR
        'time': dataSet[0],
        'cal': dataSet[1],
        'fat': dataSet[2],
        'minHR': dataSet[3],
        'maxHR': dataSet[4],
        'avgHR': dataSet[5]
    })
    
    with open('calcData.txt', 'w') as outfile:
        json.dump(data_to_send, outfile)
    

def send_data(fileName):
    
    url = 'http://pi.calebmcd.com:1880/data'
    files = {'files:': open(fileName, 'rb')}
         
    response = requests.post(url, files=files)
 
    print(response.status_code)

#.....
#.....
#.....

data = [5.3,123,78,62,167,122]
# time, cal, fat, minHR, maxHR, avgHR

store_data(data)
send_data(os.path.basename('calcData.txt'))

print("Data Sent: \n")
with open('calcData.txt') as json_file:
    file = json.load(json_file)
    for p in file['workout']:
        print('Time: ' + str(p['time']))
        print('Cal: ' + str(p['cal']))
        print('Fat: ' + str(p['fat']))
        print('minHR: ' + str(p['minHR']))
        print('maxHR: ' + str(p['maxHR']))
        print('avgHR: ' + str(p['avgHR']))
        print('')