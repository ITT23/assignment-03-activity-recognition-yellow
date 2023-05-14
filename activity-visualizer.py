# this program visualizes activities with pyglet

#import activity-recognizer as activity
#import pyglet
# this program recognizes activities

import pandas as pd
import numpy as np
import os
import re
# install scikit-learn
from sklearn import svm
import pyglet
from DIPPID import SensorUDP
from threading import Thread
from time import sleep
from dippid_data_handler import Data_Handler
from sklearn.preprocessing import scale, StandardScaler, MinMaxScaler
from pyglet.window import Window
from pyglet import app, image, clock

from activity_recognizer import Recognizer

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
INPUT_TEXT = 'Press 1 button to start recognition'
JUMPING_TEXT = 'you are jumping'
SHAKING_TEXT = 'you are shaking the phone'

PORT = 5700
sensor = SensorUDP(PORT)

jumping_data = []
shaking_data = []
lying_data = []

scaler = None

data_handler = Data_Handler()
recognizer = Recognizer()

recognizer.train_classifier()


label = None
predicted_motion = ""

# game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

def handle_accelerometer(data):
    data_handler.update_accelorometer_data(data)

sensor.register_callback('accelerometer', handle_accelerometer)

@window.event
def on_draw():

    window.clear()
    

def wait():
    sleep(3)

def gather_data(dt):
    global predicted_motion

    time_thread = Thread(target=wait, daemon=True)
    time_thread.start()
    data_x = []
    data_y = []
    data_z = []

    while(time_thread.is_alive()):
        data_x.append(data_handler.get_accelorometer_value('x'))
        data_y.append(data_handler.get_accelorometer_value('y'))
        data_z.append(data_handler.get_accelorometer_value('z'))
        sleep(0.02)
        
    predicted_motion = recognizer.classify(data_x, data_y, data_z)
    print(predicted_motion)




# latency of input sound
clock.schedule_interval(gather_data, 3.1)

# run game
app.run()


#main()