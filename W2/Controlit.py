#This code demonstrates a simple GUI being used to control an eBot

#There are known issues with synchronizing command sending, as occasionally commands are missed

# Copyright (c) 2014, Erik Wilhelm
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
   # notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
   # notice, this list of conditions and the following disclaimer in the
   # documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
   # must display the following acknowledgement:
   # This product includes software developed by Edgebotix.
# 4. Neither the name of the SUTD nor Edgebotix nor the
   # names of its contributors may be used to endorse or promote products
   # derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY ERIK WILHELM ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL ERIK WILHELM BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from Tkinter import * #import Tkinter GUI library
from eBot import eBot
from eBot import * #import eBot library
from time import sleep
    
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot.eBot()

myEBot.connect()
myvalue = [0, 0, 0, 0, 0, 0] #initialize values used to report sonar 
myEBot.halt() #stop bot

count=0; #global variable defining number of cycles for each action

def Up():
    print 'UP'
    global count
    print count
    count=1;
    while (count<10): #wait hard coded cycles going forward on button push
        sonars = myEBot.robot_uS()
        if sonars[2] < 0.300: #stop if front facing sonar detects obstacle
            myEBot.halt()
            count=count+1
            print sonars
        else: #otherwise proceed forward at full speed
            myEBot.wheels(1, 1)
            count=count+1
            print sonars
            
    myEBot.wheels(0, 0)
    
	
def Down():
    print 'DOWN'
    global count
    print count
    count=1;
    while (count<10): #wait hard coded cycles going backward on button push
        sonars = myEBot.robot_uS()
        if sonars[2] < 0.300:
            myEBot.halt()
            count=count+1
            print sonars
        else:
            myEBot.wheels(-1, -1)
            count=count+1
            print sonars
    myEBot.wheels(0, 0)

def Left():
    
    print 'LEFT'
    global count
    print count
    count=1;
    while (count<3): #wait hard coded cycles turning left on button push
        sonars = myEBot.robot_uS()
        if sonars[2] < 0.300:
            myEBot.halt()
            count=count+1
            print sonars
        else:
            myEBot.wheels(-1, 1)
            count=count+1
            print sonars
    myEBot.wheels(0, 0)

def Right():
    
    print 'RIGHT'
    global count
    print count
    count=1;
    while (count<3): #wait hard coded cycles turning right on button push
        sonars = myEBot.robot_uS()
        if sonars[2] < 0.300:
            myEBot.halt()
            count=count+1
            print sonars
        else:
            myEBot.wheels(1, -1)
            count=count+1
            print sonars
    myEBot.wheels(0, 0)

def Stop():
    myEBot.wheels(0, 0)
    myEBot.halt()
    myEBot.close()
    print 'STOP'

#cycle LED to test function
sleep(1)
myEBot.led(1)
sleep(1)
myEBot.led(0)
sleep(1)


appWindow = Tk() # creates the application window (you can use any name)
appWindow.wm_title("eBot CONTROL") #Makes the title that will appear in the top left
appWindow.config(bg = "#828481")


#Control Frame and its contents
controlFrame = Frame(appWindow, width=150, height = 200, bg="#037481", highlightthickness=2, highlightbackground="#111") #defines the control frame
controlFrame.grid() #positions the control frame with the corresponding parameters

btnFrame = Frame(controlFrame, width=150, height = 200, bg="#037481")# defines the button frame with these characteristics
btnFrame.grid() #positions the button frame inside which control buttons will reside

about = "eBOT CONTROL"
name = Label(btnFrame, width=12, height=1, text=about, font="bold", justify=CENTER, bg="#037481")
name.grid(row=0, column=2)

upBtn = Button(btnFrame, text="UP", command=Up, bg="green") #defines the UP button
upBtn.grid(row=2, column=2, padx=5, pady=5) #positions the UP button within the button frame

downBtn = Button(btnFrame, text="DOWN", command=Down, bg="yellow") #defines the DOWN button
downBtn.grid(row=4, column=2, padx=5, pady=5) #positions the UP button within the button frame

leftBtn = Button(btnFrame, text="LEFT", command=Left, bg="orange") #defines the LEFT button
leftBtn.grid(row=3, column=0, padx=5, pady=5) #positions the LEFT button within the button frame

rightBtn = Button(btnFrame, text="RIGHT", command=Right, bg="blue") #defines the RIGHT button
rightBtn.grid(row=3, column=3, padx=5, pady=5) #positions the RIGHT button within the button frame

stopBtn = Button(btnFrame, text="QUIT", command=Stop, bg="red") #defines the STOP button
stopBtn.grid(row=3, column=2, padx=5, pady=5) #positions the STOP button within the button frame


appWindow.mainloop()# begins main loop