from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import csv

filename = "vibration.csv"
header = ['acc_x', 'acc_y', 'acc_z', 'time']

sense = SenseHat()
# timestamp = datetime.now()
# delay = 0.05

def get_acc_data():
    data = []
    acc = sense.get_accelerometer_raw()
    data.append(acc["x"])
    data.append(acc["y"])
    data.append(acc["z"])
    data.append(datetime.now())
    return(data)

# print(get_acc_data())

with open(filename, 'w', newline = '') as f:
    data_writer = writer(f)
    data_writer.writerow(header)

    while True:
        data_writer.writerow(get_acc_data())
