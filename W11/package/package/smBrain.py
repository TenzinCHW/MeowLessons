import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
import time

class MySMClass(sm.SM):
    def getNextValues(self, state, inp):
        data = inp.sonars
        an = inp.analogInputs
        od = inp.odometry
        temp = inp.temperature
        ldr = inp.light
        print data
        print an
        print od
        print temp
        print ldr

        return (state, io.Action(fvel = 0.1, rvel = 0.0))
        #return (state, io.Action(fvel = 0.05, rvel = 0.05))

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

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
