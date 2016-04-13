__author__ = 'HanWei'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import firebase

url = "https://flickering-fire-1661.firebaseio.com/"  # URL to Firebase
token = "ZpSWTZaRaODNivf2S3Vil0a50BAPjx1ZhGsVbL2S"
firebase = firebase.FirebaseApplication(url, token)


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
            if instance.id == 'yellow':
                firebase.put('/ledcontroller/', 'yellow', 'on')
                # GPIO.output(yellow, GPIO.HIGH)
            else:
                firebase.put('/ledcontroller/', 'red', 'on')
                # GPIO.output(red, GPIO.HIGH)

        else:
            instance.text = 'off'
            if instance.id == 'yellow':
                firebase.put('/ledcontroller/', 'yellow', 'off')
                # GPIO.output(yellow, GPIO.LOW)
            else:
                firebase.put('/ledcontroller/', 'red', 'off')
                # GPIO.output(red, GPIO.LOW)


# The Pi does not seem to be able to run Kivy, and therefore I am writing instructions to firebase and then
# Reading it off the Pi to turn the LEDs on and off

Ledcontroller().run()
