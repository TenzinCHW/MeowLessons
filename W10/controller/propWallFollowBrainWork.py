import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist

reload(gfx)

######################################################################
#
#            Brain SM
#
######################################################################

desiredLeft = 0.75
forwardVelocity = 0.1

# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        distance = inp.sonars[0]
        print "Distance to wall: %.03f" % distance
        return (state, distance)

# inp is the distance to the right
class WallFollower(sm.SM):
    def getNextValues(self, state, inp):
        k = 0.1
        print k*(inp-desiredLeft) #k*(desiredRight-inp)
        return state,io.Action(fvel=forwardVelocity,rvel = k*(inp-desiredLeft))
#################
# Your code here
################
        pass

mySM = sm.Cascade(Sensor(), WallFollower())

######################################################################
#
#            Running the robot
#
######################################################################

def plotDist():
    func = lambda: sonarDist.getDistanceRight(io.SensorInput().sonars)
    robot.gfx.addStaticPlotFunction(y=('d_o', func))

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    plotDist()
    robot.behavior = mySM
    robot.behavior.start(traceTasks = robot.gfx.tasks())

def step():
    robot.behavior.step(io.SensorInput()).execute()

def brainStart():
    # Do this to be sure that the plots are cleared whenever you restart
    robot.gfx.clearPlotData()

def brainStop():
    pass

def shutdown():
    pass

