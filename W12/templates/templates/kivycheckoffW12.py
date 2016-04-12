__author__ = 'HanWei'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Ledcontroller(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Yellow LED'))
        yellow = Button(text='off', on_press=self.LEDpress)
        layout.add_widget(yellow)
        layout.add_widget(Label(text='Red LED'))
        red = Button(text='off', on_press=self.LEDpress)
        layout.add_widget(red)
        return layout

    def LEDpress(self, instance):
        if instance.text == 'off':
            instance.text = 'on'
        else:
            instance.text = 'off'


Ledcontroller().run()
