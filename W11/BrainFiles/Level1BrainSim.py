import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist
from time import sleep, time

######################################################################
#
#            Brain SM
#
######################################################################

desiredtheta = 0
forwardVelocity = 0.08


# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):

        return state, [inp.sonars,inp.odometry.theta]


# inp is the distance to the right
class WallFollower(sm.SM):
    startState = [0,"Corridor",0,["Straight","Straight","X"]]
    def getNextValues(self, state, inp):




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
