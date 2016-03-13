from eBot import eBot
from time import sleep
import firebase

url = "https://flickering-fire-1661.firebaseio.com/" # URL to Firebase database
token = "ZpSWTZaRaODNivf2S3Vil0a50BAPjx1ZhGsVbL2S" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

# Use a variable to determine whether there is any valid movement commands in
# the Firebase database.
no_commands = True

while no_commands:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Get movement list from Firebase
    movement_list = None

    # Write your code here
    movement_list = firebase.get('/movements')
    if movement_list != None:
        break
    sleep(0.5)

# Write the code to control the eBot here
def f():
    ebot.wheels(1,1)
    sleep(1)
def l():
    ebot.wheels(-1,1)
    sleep(1)
def r():
    ebot.wheels(1,-1)
    sleep(1)

for i in movement_list:
    if i == 'left':
        l()
    elif i == 'right':
        r()
    elif i == 'up':
        f()
ebot.wheels(0,0)
ebot.disconnect() # disconnect the Bluetooth communication
