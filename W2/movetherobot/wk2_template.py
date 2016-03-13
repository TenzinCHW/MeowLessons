# Import eBot and time module
from eBot import eBot
from time import sleep

def forward(speed, duration):
    ebot.wheels(speed,speed)
    sleep(duration)
def circle(duration):
    ebot.wheels(1,-1)
    sleep(duration)

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

############### Start writing your code here ################
circle(20)
#forward(1,5)
a = ebot.temperature()
print "The temperature is %.3f." % a
########################## end ############################## 

ebot.disconnect() # disconnect the Bluetooth communication
