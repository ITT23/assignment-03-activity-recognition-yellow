# INSTRUCTION (for M5STACK or the DIPPID App):
#   
#   - Button 1: record jumping
#   - Button 2: record lying
#   - Button 3: record shaking
#
# 
# RECORDED SENSOR:
#
#   - accelerometer
#
# RECORDING:
#
# - after buttonpress the recording lasts for 3 seconds
# - recorded values: accelerometer x, y and z axis, timestamp and the activity
# - recorded data is stored in the data folder

import uuid
import pandas as pd
from os import path
from DIPPID import SensorUDP
from time import sleep
from datetime import datetime
from threading import Thread
# own classes
from dippid_data_handler import Data_Handler
from activity_enum import Activity

# path for the data folder in which the recorded activities are stored as a csv file
CSV_DATA_PATH = path.join(path.dirname(__file__), "data\\")
# time period for the recording
RECORD_DURATION = 3
# time period for the values inbetween the recording
RECORD_DURATION_VALUES = 0.1

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

# used to save and get data like accelorometer, activity status and label
data_handler = Data_Handler()

# saves the new accelormeter data
def handle_accelerometer(data):
    data_handler.update_accelorometer_data(data)

def handle_button_1(data):
    # saves new data
    data_handler.update_button_1_data(data)
    # set the activity label to 'jumping'
    data_handler.update_activity_label(Activity.JUMPING.value)
    # notify that a activity is happening
    data_handler.set_activity_status(True)

# saves the new button 2 data
def handle_button_2(data):
    # saves new data
    data_handler.update_button_2_data(data)
    # set the activity label to 'lying'
    data_handler.update_activity_label(Activity.LYING.value)
     # notify that a activity is happening
    data_handler.set_activity_status(True)

# saves the new button 3 data
def handle_button_3(data):
    # saves new data
    data_handler.update_button_3_data(data)
    # set the activity label to 'shaking'
    data_handler.update_activity_label(Activity.SHAKING.value)
     # notify that a activity is happening
    data_handler.set_activity_status(True)

# update data everytime new data get received from the DIPPID device
sensor.register_callback('accelerometer', handle_accelerometer)
sensor.register_callback('button_1', handle_button_1)
sensor.register_callback('button_2', handle_button_2)
sensor.register_callback('button_3', handle_button_3)

def main():
    while(True):
        # if a activity is going to happen
        if data_handler.is_activity_status():
            # get the recorded data (for the recorded time period)
            data = capture_accelerometer_data()
            # get the activity label (string)
            activity = data_handler.get_activity()

            # create a csv file containing the accelerometer data, timestamp and activity label
            activity_df = pd.DataFrame(list(zip(data[0], data[1], data[2], data[3], data[4])))
            activity_df.columns = ['timestamp', 'acc_x', 'acc_y', 'acc_z', 'activity_label']
            activity_df.to_csv(f"{CSV_DATA_PATH}{activity}_{str(uuid.uuid4())}.csv") # file name -> name of the activity_ + unique id

            # notify that no activity is needed to be recorded
            data_handler.set_activity_status(False)
            data_handler.update_activity_label(Activity.NONE.value)
    
# recording time
def wait():
    sleep(RECORD_DURATION)

# get all necessary data for the csv file
def capture_accelerometer_data():
    # check if the sensor has the needed capabilities
    if(not sensor.has_capability('accelerometer') or \
       not sensor.has_capability('button_1') or \
        not sensor.has_capability('button_2') or \
            not sensor.has_capability('button_3')):
        print('missing capability')
        return
    
    else:
        data_x = []
        data_y = []
        data_z = []
        data_time_log = []
        data_activity = []
        
        time_thread = Thread(target=wait, daemon=True)
        time_thread.start() #start a thread that activates and deactivates buttons

        while(time_thread.is_alive()):
            data_time_log.append(datetime.now())
            data_x.append(data_handler.get_accelorometer_value('x'))
            data_y.append(data_handler.get_accelorometer_value('y'))
            data_z.append(data_handler.get_accelorometer_value('z'))
            data_activity.append(data_handler.get_activity())
            sleep(RECORD_DURATION_VALUES)
        
        return [data_time_log, data_x, data_y, data_z, data_activity]
 
main()