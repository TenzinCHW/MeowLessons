import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.3
forwardVelocity = 0.08


# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        v = sonarDist.getDistanceRight(inp.sonars)
        print 'Dist from robot center to wall on right', v
        return (state, v)


# inp is the distance to the right
class WallFollower(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        k1 = 30
        k2 = -29.97
        rvel = k1 * (desiredRight - inp) + k2 * state
        return ((desiredRight - inp), io.Action(fvel=forwardVelocity, rvel=rvel))
        pass


sensorMachine = Sensor()
sensorMachine.name = 'sensor'
mySM = sm.Cascade(sensorMachine, WallFollower())


######################################################################
#
#            Running the robot
#
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    robot.gfx.addStaticPlotSMProbe(y=('rightDistance', 'sensor',
                                      'output', lambda x: x))
    robot.behavior = mySM
    robot.behavior.start(traceTasks=robot.gfx.tasks())


def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())


def brainStop():
    pass
