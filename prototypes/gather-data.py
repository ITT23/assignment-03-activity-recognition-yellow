# this program gathers sensor data

# TODO: 
# - pyglet oder input Abfrage im Terminal (müssen das label abfragen)
#   -> user sollen ein label eingeben (z.B. standing) -> mithilfe von data_handler.update_motion_label(hier Input als String) wird dann das zu aufzeichnende label aktualisiert.
#   -> Start/Stop Funktion/Button rein (Aufzeichnung automatisch beenden nach z.B. 5 oder 10 Sekunden)
# - Nach der Aufnahme vom Sensor disconnecten (bei Aufnahme wieder connecten)

import pandas as pd
from pyglet import app, clock
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

# used to save and get data like accelorometer/gyroscope data, motion label and record status
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

# saves data in the motion-data.csv
def dataToCSV(dt):
    # column names for the csv file
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
    
    # used for the creation of a new csv file or for an existing but empty csv file
    empty_df = pd.DataFrame(motion_data_columns)

    # check if csv file exists -> if not -> create a empty csv file
    if not path.exists(CSV_DATA_PATH):
        empty_df.to_csv(CSV_DATA_PATH)

    # check if file is empty -> if empty -> create columns
    try:
        motion_df = pd.read_csv(CSV_DATA_PATH)
    except:
        empty_df.to_csv(CSV_DATA_PATH)

    # used to save the timestamp for every recording
    timestamp = datetime.now()
    
    # if file is not empty -> save timestamp, x/y/z accelorometer and gyroscope values and motion label
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

# write the recorded date every 0.1 second (for now it's running constantly; later it should just run if record is started)
clock.schedule_interval(dataToCSV, 0.1)

# run game
app.run()


