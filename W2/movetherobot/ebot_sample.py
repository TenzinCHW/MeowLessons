# Import eBot and time module
from eBot import eBot
from time import sleep

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

ebot.wheels(1, 1) # make the robot move at 100% speed on both wheels
sleep(5) # wait for 5 seconds

ebot.wheels(-0.5, 0) # make the robot turn counter-clockwise with left wheel at 50% speed
sleep(2) # wait for 2 seconds

ebot.led(False) # turn on the center LED on eBot
sleep(2) # wait for 2 seconds
ebot.led(True) # turn on the center LED on eBot
sleep(2) # wait for 2 seconds

ebot.disconnect() # disconnect the Bluetooth communication
