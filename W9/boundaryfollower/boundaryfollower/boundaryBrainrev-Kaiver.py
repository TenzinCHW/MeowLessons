import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io


class MySMClass(sm.SM):
    startState = 0
    old_left, old_right = [-1, -1]

    def getNextValues(self, state, inp):
        left, fleft, front, fright, right, back = inp.sonars[:6]
        print inp.sonars
        if state == 0: #Head Straight until find wall
            print "state 0"
            if front <=0.26 or fleft <= 0.1:
                nextstate = 1
                return (nextstate, io.Action(fvel=0.2, rvel=-0.2))
            elif fleft > 0.5 and left < 0.5:
                nextstate = 2
                return (nextstate, io.Action(fvel=0.2, rvel=0.2))
               
            return (state, io.Action(fvel=0.1, rvel=0.00)) 

        elif state == 1: #Turn clockwise, align to wall
            print "turning anti clockwise"
            if fleft >0.1 and front >0.36:
                return (0, io.Action(fvel=0.2, rvel=0))
            return (state, io.Action(fvel=0.0, rvel=-0.2))
        elif state == 2: #Outer turns
            print "turning clockwise"
            if fleft < 0.2:
                return (0, io.Action(fvel=0.03, rvel=0))
            return (state, io.Action(fvel=0.0, rvel=0.2))
        #one more state for left turning required just in case our bot gets lost somehow
        else:
            return (0, io.Action(fvel=0.2, rvel=0.00))  


mySM = MySMClass()
mySM.name = 'brainSM'


######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar' + str(sonarNum),
                                        lambda:
                                        io.SensorInput().sonars[sonarNum]))


# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True,  # slime trails
                                  sonarMonitor=False)  # sonar monitor widget

    # set robot's behavior
    robot.behavior = mySM


# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks())


# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())


# called when the stop button is pushed
def brainStop():
    pass


# called when brain or world is reloaded (before setup)
def shutdown():
    pass
