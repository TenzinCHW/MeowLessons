import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

# fin = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\W9\ebotcalib1.txt','w')
class MySMClass(sm.SM):
    startState = 'Charge ahead'

    def getNextValues(self, state, inp):
        left,fleft,front,fright,right,back,UK1,UK2 = inp.sonars
        if state == 'Charge ahead':
            if front <= 0.3 and fright > 0.3:
                nextstate = 'Follow obstacle on right'
                spd = [0,0.2]
                # return nextstate,io.Action(fvel=0,rvel=0.2)
            elif front > 0.3:
                nextstate = state
                spd = [0.1,0]
                # return nextstate,io.Action(fvel=0.1,rvel=0)
            return state,io.Action(fvel=spd[0],rvel=spd[1])
        elif state == 'Follow obstacle on right':
            if right >= 0.3:
                nextstate = state
                return nextstate,io.Action(fvel=0.1,rvel=-0.1)
            elif right <= 0.2:
                nextstate = 'Charge ahead'
                return nextstate,io.Action(fvel=0.1,rvel=0)

        # elif state == 'Follow closer':
        #     if right <= 0.25:
        #         nextstate = 'Follow obstacle on right'
        #         return nextstate,io.Action(fvel=0.1,rvel=)
        # fin.write(inp.sonars[1:4])
        print inp.sonars  # list
        # print inp.odometry.theta
        return (state, io.Action(fvel=0, rvel=0))


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
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False,  # slime trails
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
