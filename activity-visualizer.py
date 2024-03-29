# this program visualizes activities with pyglet

from os import path
import pyglet
from DIPPID import SensorUDP
from threading import Thread
from time import sleep
from dippid_data_handler import Data_Handler
from pyglet.window import Window
from pyglet import app, image, clock
# own class
from activity_recognizer import Recognizer

# game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# background image path
BACKGROUND_IMAGE_PATH = path.join(path.dirname(__file__), "pictures\\background.jpg") # https://www.pexels.com/de-de/foto/hochwinkelfoto-des-roboters-2599244/ @Alex Knight
# waving image path
WAVING_IMAGE_PATH = path.join(path.dirname(__file__), "pictures\waving.jpeg") # https://www.pexels.com/de-de/foto/mann-im-gestreiften-hemd-winkt-1035835/ @Nicholas Githiri 
# jumping image path
JUMPING_IMAGE_PATH = path.join(path.dirname(__file__), "pictures\jumping.jpeg") # https://www.pexels.com/de-de/foto/mann-von-der-strasse-springen-1631917/ @Bruno Henrique 
# lying image path
LYING_IMAGE_PATH = path.join(path.dirname(__file__), "pictures\lying.jpeg") # https://www.pexels.com/de-de/foto/frau-die-auf-weissem-stuhl-beim-lesen-des-buches-liegt-1537317/ @Adrienn 

# time period for collecting data
DURATION_MOTION = 3
# frequency of data collection
DURATION_VALUE_RECORD = 0.02

PREDICTION_CAPTION = "YOUR PREDICTED MOTION IS:"

PORT = 5700
sensor = SensorUDP(PORT)

# handles DIPPID data 
data_handler = Data_Handler()
# trains model and provides classifier
recognizer = Recognizer()
recognizer.train_classifier()
# predicted motion
predicted_motion = ""

def handle_accelerometer(data):
    data_handler.update_accelorometer_data(data)

sensor.register_callback('accelerometer', handle_accelerometer)

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

@window.event
def on_draw():

    window.clear()
    # draw background
    draw_background_img()
    # draw image for the corresponding motion
    draw_motion_img(predicted_motion)
    # draw caption
    draw_prediction_caption()

def draw_prediction_caption():

    prediction_caption_label = pyglet.text.Label(PREDICTION_CAPTION,
                          font_name='Times New Roman',
                          font_size=30,
                          x = WINDOW_WIDTH / 2,
                          y = WINDOW_HEIGHT * 0.9,
                          color=(0,255,255,255),
                          anchor_x='center', anchor_y='center')

    prediction_caption_label.draw()

def draw_motion_img(motion_string):
    motion_img_path = ""

    if motion_string == 'jumping':
        motion_img_path = JUMPING_IMAGE_PATH
    elif motion_string == 'waving':
        motion_img_path = WAVING_IMAGE_PATH
    elif motion_string == 'lying':
        motion_img_path = LYING_IMAGE_PATH

    if motion_string != "":
        motion_image = image.load(motion_img_path)
        motion_image.blit(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT * 0.1)

def draw_background_img():
    motion_image = image.load(BACKGROUND_IMAGE_PATH)
    motion_image.blit(0, 0)

def wait():
    sleep(DURATION_MOTION)

# gather data for 3 seconds and then predict the motion
def gather_data(dt):
    global predicted_motion

    if(sensor.has_capability('button_1')):

        time_thread = Thread(target=wait, daemon=True)
        time_thread.start()
        data_x = []
        data_y = []
        data_z = []

        while(time_thread.is_alive()):
            data_x.append(data_handler.get_accelorometer_value('x'))
            data_y.append(data_handler.get_accelorometer_value('y'))
            data_z.append(data_handler.get_accelorometer_value('z'))
            sleep(DURATION_VALUE_RECORD)
        predicted_motion = recognizer.classify(data_x, data_y, data_z)

clock.schedule_interval(gather_data, DURATION_MOTION)

# run game
app.run()

