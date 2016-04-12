__author__ = 'HanWei'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)
red = 5
yellow = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)


class Ledcontroller(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Yellow LED'))
        yellow = Button(text='off', id='yellow', on_press=self.LEDpress)
        layout.add_widget(yellow)
        layout.add_widget(Label(text='Red LED'))
        red = Button(text='off', on_press=self.LEDpress)
        layout.add_widget(red)
        return layout

    def LEDpress(self, instance):
        if instance.text == 'off':
            instance.text = 'on'
            if instance.id=='yellow':
                GPIO.output(yellow, GPIO.HIGH)
            else:
                GPIO.output(red, GPIO.HIGH)

        else:
            instance.text = 'off'
            if instance.id=='yellow':
                GPIO.output(yellow, GPIO.LOW)
            else:
                GPIO.output(red, GPIO.LOW)


Ledcontroller().run()
