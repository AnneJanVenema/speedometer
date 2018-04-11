# Set window size
import kivy
kivy.require('1.9.0')
from kivy.config import Config

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

# Config.set('graphics', 'width', '240')
# Config.set('graphics', 'height', '400')
 
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.slider import Slider

from kivy.animation import Animation
from kivy.properties import ListProperty, NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp, sp
from kivy.core.window import Window
from random import random

# Set background color
Window.clearcolor = (0, 0, 0, 1)

# Import kv files
from kivy.lang import Builder
Builder.load_file('assets/kv/speed.kv')

speed = 1
speeDir = True
leverLeft = True
second = 'asd'

from subprocess import check_output

scanoutput = check_output(["iwlist", "wlan0", "scan"])

ssid = "WiFi not found"

for line in scanoutput.split():
  line = line.decode("utf-8")
  if line[:5]  == "ESSID":
    ssid = line.split('"')[1]

print(ssid)

class speedoMeter(FloatLayout):

    color = ListProperty ([1,1,1]);

    def __init__(self, **kwargs):
        super(speedoMeter, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/4)
 
    def func(self):
        self.ids['asdasdasd'].col = (0,1,0,1)

    def update(self, dt):
        global speed
        global speeDir
        global second

        wtd = NumericProperty(1)
        penrad = NumericProperty(10)
        pencolor = ListProperty([1, 0, 0, 1])

        if speed > 6:
            # self.
            with self.canvas:
                Color(rgba=([1, 0, 0, 1]))

        if speed > 40:
            self.color = [1,0,0]

        else:
            self.color = [1,1,1]

        if speed > 98:
            speed = 1

        if speeDir:
            speed += 1

        number = str(speed)
        if speed > 9:
            currentID = 'num_' + number[0]
            currentID2 = 'num2_' + number[1]

            self.ids['num_1'].opacity = 0
            self.ids['num_2'].opacity = 0
            self.ids['num_3'].opacity = 0
            self.ids['num_4'].opacity = 0
            self.ids['num_5'].opacity = 0
            self.ids['num_6'].opacity = 0
            self.ids['num_7'].opacity = 0
            self.ids['num_8'].opacity = 0
            self.ids['num_9'].opacity = 0
            self.ids[currentID].opacity = 1

            self.ids['num2_0'].opacity = 0
            self.ids['num2_1'].opacity = 0
            self.ids['num2_2'].opacity = 0
            self.ids['num2_3'].opacity = 0
            self.ids['num2_4'].opacity = 0
            self.ids['num2_5'].opacity = 0
            self.ids['num2_6'].opacity = 0
            self.ids['num2_7'].opacity = 0
            self.ids['num2_8'].opacity = 0
            self.ids['num2_9'].opacity = 0
            self.ids[currentID2].opacity = 1

        else: 
            self.ids['num_0'].opacity = 1
            currentID2 = 'num2_' + number[0]
            self.ids['num2_0'].opacity = 0
            self.ids['num2_1'].opacity = 0
            self.ids['num2_2'].opacity = 0
            self.ids['num2_3'].opacity = 0
            self.ids['num2_4'].opacity = 0
            self.ids['num2_5'].opacity = 0
            self.ids['num2_6'].opacity = 0
            self.ids['num2_7'].opacity = 0
            self.ids['num2_8'].opacity = 0
            self.ids['num2_9'].opacity = 0
            self.ids[currentID2].opacity = 1



class brakeLever(FloatLayout):
    global speed

    def __init__(self, **kwargs):
        super(brakeLever, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def brakeRight(self, status):
        for i in range(1,5):
            breakLeverID = 'breakLeverRight_'+ str(i)
            breakLeverAnim = Animation(duration = 0.1 - .025 * i) 
            if status == 'up':
                breakLeverAnim += Animation(pos_hint = { 'center_y': .5, 'x': (i/4)+.11 }, opacity = 1, duration = .22, t='in_out_quint') 
            if status == 'down':
                breakLeverAnim += Animation(pos_hint = { 'center_y': .5, 'x': (i)/4 }, opacity = 0, duration = .22, t='in_out_quint')
            breakLeverAnim.start(self.ids[breakLeverID])

    def brakeLeft(self, status):
        for i in range(1,5):
            breakLeverID = 'breakLeverLeft_'+ str(i)
            breakLeverAnim = Animation(duration = 0.1 - .025 * i) 
            if status == 'up':
                breakLeverAnim += Animation(pos_hint = { 'center_y': .5, 'center_x': 1-(i/4)-.11 }, opacity = 1, duration = .22, t='in_out_quint')
            if status == 'down':
                breakLeverAnim += Animation(pos_hint = { 'center_y': .5, 'center_x': 1-(i/4) }, opacity = 0, duration = .22, t='in_out_quint')
            breakLeverAnim.start(self.ids[breakLeverID])

    def brakeMessage(self, status):
        if status == 'up':
            anim = Animation(y = 0, opacity = 1, duration = .5, t='in_out_quint')
        if status == 'down':
            anim = Animation(y = 10, opacity = 0, duration = .2, t='out_back')
        anim.start(self.ids['breakLeverMessage'])

    def update(self, dt):
        if speed > 40: #if GPIO.input(leverLeft) == True:
            self.brakeRight('up')
            self.brakeLeft('up')
            self.brakeMessage('up')

        else:
            self.brakeRight('down')
            self.brakeLeft('down')
            self.brakeMessage('down')



# Define rootwidget
class cittaApp(FloatLayout, App):
    print(kivy.__version__)
    def build(self):
        inputDisplay = speedoMeter()
        inputDisplay2 = brakeLever()
        layout = FloatLayout()

        layout.add_widget(inputDisplay)
        layout.add_widget(inputDisplay2)
        return layout



# Initialise speedometer app
if __name__ == '__main__':
    cittaApp().run()






