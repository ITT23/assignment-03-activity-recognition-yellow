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

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

# window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def handle_accelerometer(data):
    print(data)

def handle_gyroscope(data):
    print(data)

sensor.register_callback('accelerometer', handle_accelerometer)
sensor.register_callback('gyroscope', handle_gyroscope)
#sensor.register_callback('gyroscope', handle_accelerometer)

# create game window
#window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)


