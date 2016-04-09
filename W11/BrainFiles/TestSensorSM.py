import libdw.sm as sm
import math
import libdw.util as util
from soar.io import io
import libdw.gfx as gfx
import libdw.eBotsonarDist as sonarDist


class WallFollower(sm.SM):
    startState = [0,0,0,0,[[],[],[],[],[],[]]]
    def getNextValues(self, state, inp):
        if len(state[4][0]) < 8:
            for i in range(6):
                state[4][i] = replaceghost(state[4][i], inp.sonars[i])
            print 'hi'
            return state, io.Action(fvel=0,rvel=0)
        else:
            for i in range(6):
                state[4][i] = replaceghost(state[4][i], inp.sonars[i])
        left, fleft, front, fright, right, back = state[4]
        return state, io.Action(fvel=0,rvel=0)



def replaceghost(current, new):
    if len(current) < 10:
        current.append(new)
        return current
    else:
        del current[0]
        current.append(new)
        sortedcurrent = sorted(current)
        average = sum(sortedcurrent)/len(sortedcurrent)
        for i in range(len(current)-2):
            if abs(current[i+1] - average) > 0.3:
                del current[i+1]
    return current


robo = WallFollower()
mySM = robo

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