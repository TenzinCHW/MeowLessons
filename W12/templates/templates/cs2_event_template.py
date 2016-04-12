from kivy.app import App
from kivy.uix.label import Label


class SlideDetectApp(App):
    def build(self):
        self.main = Label(text='Slide me!',on_touch_move=self.detect)
        # self.main.bind(on_touch_move=self.detect)
        self.main.bind(on_touch_up=self.goback)
        return self.main

    def detect(self, instance, touch):
        if not instance.collide_point(touch.x, touch.y):
            return False
        if touch.dx < -40:
            self.main.text = 'Slide left'
        if touch.dx > 40:
            self.main.text = 'Slide right'
        if touch.dy < -40:
            self.main.text = 'Slide down'
        if touch.dy > 40:
            self.main.text = 'Slide up'
        return True

    def goback(self, instance, touch):
        self.main.text = 'Slide me!'

if __name__ == '__main__':
    SlideDetectApp().run()
