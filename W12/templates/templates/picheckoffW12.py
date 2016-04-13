__author__ = 'HanWei'
import RPi.GPIO as GPIO
import firebase

url = "https://flickering-fire-1661.firebaseio.com/"  # URL to Firebase
token = "ZpSWTZaRaODNivf2S3Vil0a50BAPjx1ZhGsVbL2S"
firebase = firebase.FirebaseApplication(url, token)

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)
red = 5
yellow = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

while True:
    redLED = firebase.get('/ledcontroller/red')
    yellowLED = firebase.get('ledcontroller/yellow')
    if redLED == 'on':
        GPIO.output(red, GPIO.HIGH)
    if yellowLED == 'on':
        GPIO.output(yellow, GPIO.HIGH)
    if redLEO == 'off':
        GPIO.output(red, GPIO.LOW)
    if yellowLED == 'off':
        GPIO.output(yellow, GPIO.LOW)
