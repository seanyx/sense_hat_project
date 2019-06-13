from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

def get_acc_data():
    data = []
    data.append(sense.get_accelerometer_raw())
    data.append(datetime.now())
    return(data)

print(get_acc_data())
