from kivy.app import App
from kivy.uix.label import Label


class AlternateApp(App):
    c = 0
    def build(self):
        self.main = Label(text='Programming is fun.')
        self.main.bind(on_touch_down=self.alternate)
        return self.main

    def alternate(self, instance, touch):
        if self.c == 0:
            self.main.text = 'It is fun to programme.'
        else:
            self.main.text = 'Programming is fun.'
        self.c = 1-self.c

AlternateApp().run()
