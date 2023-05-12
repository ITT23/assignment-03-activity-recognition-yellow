import uuid
import csv
from os.path import isfile
from DIPPID import SensorUDP
from time import sleep, time
from threading import Thread

ACTIVITY = {
    'none' : 0,
    'jumping' : 1,
    'lying' : 2,
    'shaking' : 3,
}

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)


def main():
    while(True):
        activity = check_activity_selection()
        if(ACTIVITY[activity] != ACTIVITY['none']):
            data = capture_accelerometer_data()
            file_number = get_file_number(activity)
            # https://www.scaler.com/topics/how-to-create-a-csv-file-in-python/
            with open(f'{activity}{file_number}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['x', 'y', 'z', 'timestamp', 'activity'])
                for i in range(len(data[0])):
                    writer.writerow([data[0][i], data[1][i], data[2][i], data[3][i], activity])
                
            

def check_activity_selection():
    if(sensor.get_value('button_1') == 1):
        return 'jumping'
    elif(sensor.get_value('button_2') == 1):
        return 'lying'
    elif(sensor.get_value('button_3') == 1):
        return 'shaking'
    else:
        return 'none'
    
def get_file_number(activity):
    counter = 0
    while(isfile(f'{activity}{counter}.csv')):
        counter += 1
    return counter
    
def wait():
    sleep(1)
    
def capture_accelerometer_data():
    # check if the sensor has the 'accelerometer' capability
    if(not sensor.has_capability('accelerometer')):
        return
    data_x = []
    data_y = []
    data_z = []
    data_time_log = []
    
    time_thread = Thread(target=wait, daemon=True)
    time_thread.start() #start a thread that activates and deactivates button_1
    while(time_thread.is_alive()):
        acc_x = float(sensor.get_value('accelerometer')['x'])
        acc_y = float(sensor.get_value('accelerometer')['y'])
        acc_z = float(sensor.get_value('accelerometer')['z'])
        data_x.append(acc_x)
        data_y.append(acc_y)
        data_z.append(acc_z)
        data_time_log.append(time())
        sleep(0.01)
    
    return [data_x, data_y, data_z, data_time_log]

 
main()