import RPi.GPIO as GPIO
from time import sleep
import firebase

url = "Replace me" # URL to Firebase database
token = "Replace me" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
buttons = {'ok': 12, 'left': 16, 'up': 20, 'right': 21}

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
GPIO.setup(buttons.values(), GPIO.IN, GPIO.PUD_DOWN)

# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []

done = False

while not done:
    # Check each button to determine whether any of them has been pressed. If
    # the OK button is pressed, the program exits the while loop and writes the
    # movement_list to the Firebase database. If any of the directional buttons
    # are pressed, the commands should be stored in the movement_list.

    # Write your code here
    pass


# Write to database once the OK button is pressed

