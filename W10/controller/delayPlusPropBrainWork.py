import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist
# from xlwt import Workbook

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 1
forwardVelocity = 0.08
# with open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\W11\Braintest.txt', 'w+') as f:
#     f.write("Hello Tenzin")

# No additional delay
class Sensor(sm.SM):
        def getNextValues(self, state, inp):
            v = inp.sonars[3]
            print 'Dist from robot center to wall on right', v
            return (state, v)


    # inp is the distance to the right
class WallFollower(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        k1 = 10
        k2 = -0.977
        rvel = k1 * (desiredRight - inp) + k2 * state

        return ((desiredRight - inp), io.Action(fvel=forwardVelocity, rvel=rvel))
        pass

# for i in range(6):
        #     self.datasheet.row(self.currentrow).set_cell_number(i,inp.sonars[i])
        #     self.currentrow += 1
        # self.wb.save('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\W11\Braintest.xls')

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
