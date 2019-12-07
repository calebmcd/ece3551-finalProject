import manageData.py as myModule

data = [5.00,123,78,62,167,122]
# time, cal, fat, minHR, maxHR, avgHR

store_data(data)
send_data(os.path.basename('calcData.txt'))

