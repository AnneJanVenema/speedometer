# Set window size
import kivy
kivy.require('1.9.0')
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')
 
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


class speedoMeter(FloatLayout):

    color = ListProperty ([1,1,1]);

    def __init__(self, **kwargs):
        super(speedoMeter, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.1)
 
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

        if speed > 20:
            self.color = [1,0,0]


        if speed > 98:
            speed = 1
        if speeDir:
            speed += 1

        # b = [a[i] + a[i+1] for i in range(len(a) - 1)]

        # anim = Animation(opacity = 1, duration = 0)

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

            # anim.start(self.ids[currentID])
            # anim.start(self.ids[currentID2])

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

            # anim.start(self.ids[currentID2])



class brakeLever(FloatLayout):
    global speed

    def __init__(self, **kwargs):
        super(brakeLever, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/2)

    def brakeRight(self, brakeNum):
        if brakeNum == 4:
            breakLeverAnim = Animation(x = 213+30, duration = .2, t = 'in_out_quint') + Animation(x = 213, duration = .2, t = 'out_back')
            breakLeverAnim.start(self.ids.breakLeverRight)

        else:
            breakLeverID = 'breakLeverRight_'+ str(brakeNum)
            # self.ids[breakLeverID].x = 60 * brakeNum
            breakLeverAnim = Animation(duration = .05 * brakeNum) + Animation(x = self.ids[breakLeverID].x+60, opacity = 1, duration = .5, t='in_out_quint') + Animation(x = 60 * brakeNum, opacity = .4, duration = .3, t='in_out_quint')
            breakLeverAnim.start(self.ids[breakLeverID])

    def brakeLeft(self, brakeNum):
        breakLeverID = 'breakLeverLeft_'+ str(brakeNum)
        if brakeNum == 4:
            breakLeverAnim = Animation(x = -93-30, duration = .2, t = 'in_out_quint') + Animation(x = -93, duration = .2, t = 'out_back')
            breakLeverAnim.start(self.ids.breakLeverLeft)

        else:
            # self.ids[breakLeverID].x = 60 * brakeNum
            breakLeverAnim = Animation(duration = .05 * brakeNum) + Animation(x = self.ids[breakLeverID].x-60, opacity = 1, duration = .3, t='in_out_quint') + Animation(x = 60 * brakeNum, opacity = .4, duration = .2, t='in_out_quint')
            breakLeverAnim.start(self.ids[breakLeverID])


    def update(self, dt):

        self.brakeRight(0)
        self.brakeLeft(0)
        self.brakeRight(1)
        self.brakeLeft(1)
        self.brakeLeft(2)
        self.brakeRight(2)
        self.brakeRight(3)
        self.brakeLeft(3)
        self.brakeRight(4)
        self.brakeLeft(4)

        if speed > 20: #if GPIO.input(leverLeft) == True:
            anim = Animation(y = 0, opacity = 1, duration = .5, t='in_out_quint')
            anim.start(self.ids['breakLeverMessage'])

        else:
            anim = Animation(y = 10, opacity = 0, duration = .2, t='out_back')
            anim.start(self.ids['breakLeverMessage'])




class cittaApp(FloatLayout, App):
    print(kivy.__version__)
    def build(self):
        inputDisplay = speedoMeter()
        inputDisplay2 = brakeLever()
        layout = FloatLayout()

        layout.add_widget(inputDisplay)
        layout.add_widget(inputDisplay2)
        return layout

if __name__ == '__main__':
    cittaApp().run()






