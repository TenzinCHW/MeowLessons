import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util

dDesired = 0.7

# Input is output of Sensor machine (below); output is an action.
# Note that this machine must also compute E, the error, and output
# the velocity, based on that.
class Controller(sm.SM):
    def getNextValues(self, state, inp):
        return state,io.Action(fvel = -5*(dDesired-inp))
        pass

# Input is SensorInput instance; output is a delayed front sonar reading 
class Sensor(sm.SM):
    def __init__(self, initDist, numDelays):
        self.startState = [initDist]*numDelays
    def getNextValues(self, state, inp):
        print inp.sonars[2]
        output = state[-1]
        state = [inp.sonars[2]] + state[:-1]
        return (state, output)

mySM = sm.Cascade(Sensor(1.5, 1), Controller())
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addStaticPlotFunction(y=('sonar'+str(sonarNum),
                                 lambda: io.SensorInput().sonars[sonarNum]))

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    plotSonar(2)
    robot.behavior = mySM
    robot.behavior.start(traceTasks = robot.gfx.tasks())

def brainStart():
    pass

def step():
    robot.behavior.step(io.SensorInput()).execute()

def brainStop():
    pass

def shutdown():
    pass
