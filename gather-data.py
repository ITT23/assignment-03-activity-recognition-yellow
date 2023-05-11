# this program gathers sensor data

# TODO: 
# - DIPPID Daten empfangen
# - Sinvoll als CSV abspeichern 
# - Start - Stop zum Abspeichern
# - pyglet Anwendung

# 3 Aktivitäten: Stehen, Liegen und Winken
import pandas as pd
from pyglet import app, image, clock
from pyglet.window import Window
from DIPPID import SensorUDP
from os import path
from datetime import datetime
# own class
from dippid_data_handler import Data_Handler


# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

# path to data csv file
CSV_DATA_PATH = path.join(path.dirname(__file__), "data\motion-data.csv")

# window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

data_handler = Data_Handler()

# saves the new accelormeter data
def handle_accelerometer(data):
    data_handler.update_accelorometer_data(data)

# saves the new gyroscope data
def handle_gyroscope(data):
    data_handler.update_gyroscope_data(data)

# update data everytime new data get received
sensor.register_callback('accelerometer', handle_accelerometer)
sensor.register_callback('gyroscope', handle_gyroscope)

def dataToCSV(dt):
    
    # if file is empty
    try:
        motion_df = pd.read_csv(CSV_DATA_PATH)
    except:
        motion_data_columns = {
            'timestamp':[],
            'acc_x':[],
            'acc_y':[],
            'acc_z':[],
            'gyro_x':[],
            'gyro_y':[],
            'gyro_z':[],
            'label':[]
        }

        df = pd.DataFrame(motion_data_columns)
        df.to_csv(CSV_DATA_PATH)

    timestamp = datetime.now()
    
    # if file is not empty
    motion_data = {
        'timestamp':[timestamp],
        'acc_x':[data_handler.get_accelorometer_value('x')],
        'acc_y':[data_handler.get_accelorometer_value('y')],
        'acc_z':[data_handler.get_accelorometer_value('z')],
        'gyro_x':[data_handler.get_gyroscope_value('x')],
        'gyro_y':[data_handler.get_gyroscope_value('y')],
        'gyro_z':[data_handler.get_gyroscope_value('z')],
        'label':[data_handler.get_motion_label()]
    }

    motion_data_df = pd.DataFrame(motion_data)
    motion_data_df.to_csv(CSV_DATA_PATH, mode='a', index=False, header=False)


# create game window
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

#@window.event
#def on_draw():
    #print('filler')

clock.schedule_interval(dataToCSV, 0.2)

# run game
app.run()


