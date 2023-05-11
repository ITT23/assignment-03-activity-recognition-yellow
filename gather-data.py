# this program gathers sensor data

# TODO: 
# - DIPPID Daten empfangen
# - Sinvoll als CSV abspeichern 
# - Start - Stop zum Abspeichern
# - pyglet Anwendung

# 3 Aktivitäten: Stehen, Liegen und Winken

from pyglet import app, image, clock
from pyglet.window import Window
from DIPPID import SensorUDP
# own class
from dippid_data_handler import Data_Handler


# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

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


# create game window
#window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)


