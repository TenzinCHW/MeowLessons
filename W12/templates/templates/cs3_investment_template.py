from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Investment(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text="Investment Amount", halign='left'))
        self.amt = TextInput(multiline=False)
        layout.add_widget(self.amt)

        layout.add_widget(Label(text="Years", halign='left'))
        self.years = TextInput(multiline=False)
        layout.add_widget(self.years)

        layout.add_widget(Label(text="Annual interest rate", halign='left'))
        self.rate = TextInput(multiline=False)
        layout.add_widget(self.rate)

        layout.add_widget(Label(text="Future Value",halign='left'))
        self.txtFutureVal = Label(text='')
        layout.add_widget(self.txtFutureVal)

        btn = Button(text="Calculate", on_press=self.calculate)
        layout.add_widget(btn)
        return layout


    def calculate(self, instance):
        invAmt = float(self.amt.text) # the .text refers to the text value of the self.amt variable!
        years = float(self.years.text)
        annIntRate = float(self.rate.text)
        newval = round(invAmt*(1+annIntRate/1200.0)**(12*years),2)
        self.txtFutureVal.text = str(newval)


Investment().run()
