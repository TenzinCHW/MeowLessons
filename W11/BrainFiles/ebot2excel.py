# Import eBot and time module
from eBot import eBot
from time import sleep
from xlwt import Workbook

# Modified week 2's code to collect data from ebot
ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth
wb = Workbook()
sheet1 = wb.add_sheet('Test5-9')
rownum = 2
while True:
    ebot.wheels(0.515, 0.5) # make the robot move at 50% speed on both wheels
    reading = ebot.sonars()
    print reading
    for i in range(6):
        sheet1.row(rownum).write(i,reading[i])
    rownum += 1
    if rownum >= 400:
        wb.save('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\W11\Test5-9.xls')
    # sleep(5) # wait for 5 seconds

# ebot.wheels(-0.5, 0) # make the robot turn counter-clockwise with left wheel at 50% speed
# sleep(2) # wait for 2 seconds

# ebot.led(False) # turn on the center LED on eBot
# sleep(2) # wait for 2 seconds
# ebot.led(True) # turn on the center LED on eBot
# sleep(2) # wait for 2 seconds

ebot.disconnect() # disconnect the Bluetooth communication
