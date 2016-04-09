import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist
from time import time
import firebase
import urllib2


######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.65
desiredFront = 0.5
forwardVelocity = 0.08
k1 = 0.1
k2 = 0.095
url = "https://flickering-fire-1661.firebaseio.com/"  # URL to Firebase
token = "ZpSWTZaRaODNivf2S3Vil0a50BAPjx1ZhGsVbL2S"
firebase = firebase.FirebaseApplication(url, token)
req = urllib2.Request('http://people.sutd.edu.sg/~oka_kurniawan/10_009/y2015/2d/tests/level1_1.inp')
req.add_header('User-agent', 'SUTD 2D Demo')
res = urllib2.urlopen(req)

instructions = []
for line in res:
    instructions.append(line.strip())

map = {'S': [1, 1], 'J1': [2, 1],'C1':[3,1], 'J2':[4,1],'X':[5,1],
       'C2':[2,2],'C3':[4,2],'D':[1,3],'J3':[2,3],'C4':[3,3],'J4':[4,3],'A':[5,3],
       'B':[2,4],'C':[4,4]}

def pathplanner(instructions):
    timestovisit = {A:[0,0],B:[0,0],C:[0,0],D:[0,0]}
    path = ['S','J1','C1','J2','X']
    for i in instructions:
        if i[0] == 'A':
            timestovisit[i[0]] += int(math.ceil(int(i[1:]/6.0)))
            timestovisit[i] += int(i[1:])%6
        elif i[0] == 'B':
            B[0] += int(math.ceil(int(i[1:]/6.0)))
            B[1] += int(i[1:])%6
        elif i[0] == 'C':
            C[0] += int(math.ceil(int(i[1:]/6.0)))
            C[1] += int(i[1:])%6
        elif i[0] == 'D':
            D[0] += int(math.ceil(int(i[1:]/6.0)))
            D[1] += int(i[1:])%6
        else:
            print '%s is not a valid destination.' % i[0]
    if A[1] == 0:
        path.append('')

    return path


def turn(state,front,fleft,fright,theta):
    dir = direction(state['Location'],state['ListofDest'][0])
    revel = k1 * (dir-theta) + k1 * state['thetaerr']
    fevel = 0.3*(4-fleft) + 0.2*(state['diagerr'])
    return state,io.Action(fvel=forwardVelocity,rvel=revel)

def direction(location, destination):
    if location[0] == destination[0]:
        diff = destination[1] - location[1]
        if diff > 0:
            dir = 0
        else:
            dir = math.pi
    else:
        if destination[0] - location > 0:
            dir = -math.pi/2
        else:
            dir = math.pi/2
    return dir

def keepdist(state,Left,Right):
    revel = k1 * (Left - Right) + k2 * state[0]
    state[0] = Left - Right
    print "Using right wall to straighten"
    return state, io.Action(fvel=forwardVelocity, rvel=revel)

# todo - optimize and plan path by search (Look in dw text last chapter for search)


class RAAAR(sm.SM):
    startState = {'sideerr': 0,'diagerr':0,'thetaerr':0, 'Location':map['S'],'Next':pathplanner(instructions),'Currently':'Straight'} # Currently can be straight or turning

    def done(self, state):
        if len(state[3]) == 0:
            return True
        return False

    def getNextValues(self, state, inp):
        theta, temp, ldr = inp.odometry.theta, inp.temperature, inp.light
        left, fleft, front, fright, right, back = inp.sonars[:6]


        if state['Currently'] == 'Straight':
            if (left > 1.4 or right > 1.4) and back > 1.3:
                return turn(state,front,fleft,fright,theta)
            elif


def straighten(sonars, theta):
    desiredtheta += math.pi / 2
    if desiredtheta > 2 * math.pi:
        desiredtheta -= 2 * math.pi
    elif desiredtheta < 0:
        desiredtheta += 2 * math.pi
    if abs(desiredtheta - Theta) > 0.4:


def uploadwrite(state, sonars, theta, temp, ldr):
    fin = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\\2D\DW2DShenanigans.txt', 'a')
    now = time.strftime('%H:%M:%S') + '|' + time.strftime('%d/%m/%Y')
    othernow = time.strftime('<%H:%M:%S>') + '||' + time.strftime('<%d/%m/%Y>' + '||')
    if state[3][0] == 'A':
        fin.write(othernow + 'Expose Plates at A\n')
        firebase.put('/stationA/', 'ldr', ldr)
        firebase.put('/stationA/', 'temp', temp)
        firebase.put('/stationA/', 'time', now)
    elif state[3][0] == 'B':
        fin.write(othernow + 'Expose Plates at B\n')
        firebase.put('/stationB/', 'ldr', ldr)
        firebase.put('/stationB/', 'temp', temp)
        firebase.put('/stationB/', 'time', now)
    elif state[3][0] == 'C':
        fin.write(othernow + 'Expose Plates at C\n')
        firebase.put('/stationC/', 'ldr', ldr)
        firebase.put('/stationC/', 'temp', temp)
        firebase.put('/stationC/', 'time', now)
    elif state[3][0] == 'D':
        fin.write(othernow + 'Expose Plates at D\n')
        firebase.put('/stationD/', 'ldr', ldr)
        firebase.put('/stationD/', 'temp', temp)
        firebase.put('/stationD/', 'time', now)
    elif state[3][0] == 'X':
        if len(state[3][0]) == 1:
            fin.write(othernow + 'Finished, and arrived at X\n')
        elif len(state[3][0]) != 1:
            fin.write(othernow + 'Collect Plates at X\n')
        firebase.put('/station/', 'ldr', ldr)
        firebase.put('/stationA/', 'temp', temp)
        firebase.put('/stationA/', 'time', now)
    else:
        print 'Not a station'
    global checked
    checked = True
    fin.close()
    return state, io.Action(fvel=0, rvel=0)


def uturn(state, theta):  # todo - slow down, stop, turn ebot 180 degrees
    thetadict = {'A': math.pi, 'B': math.pi / 2, 'C': math.pi / 2, 'D': 0, 'X': math.pi}  # THIS IS FOR LEVEL 2
    error = abs(thetadict[state[3][0]] - theta)
    global turned
    if error > 0.2:
        fevel = 0
        revel = 0.15
    else:
        turned = True
        fevel = 0
        revel = 0
    return state, io.Action(fvel=fevel, rvel=revel)

    # if not checked:
    #                     timer = time()
    #                     mytime = time()  # Should be 4.3 for real ebot
    #                     checked = True
    #                     return state, io.Action(fvel=0, rvel=0)
    #                 elif time() - timer < 8:
    #                     return state, io.Action(fvel=0, rvel=0)
    #                 elif time() - mytime < 4:  # Needs calibration
    #                     return state, io.Action(rvel=0.15)
    #                 else:
    #                     timer = None
    #                     checked = False
    #                     del state[3][0]
    #                     return state, io.Action(fvel=0.1, rvel=0)
    #             else:
    #                 return followwall(state, fleft, fright, left, right)


mySM = RAAAR()


######################################################################
#
#            Running the robot
#
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False,
                                  sonarMonitor=True)
    robot.gfx.addStaticPlotSMProbe(y=('rightDistance', 'sensor',
                                      'output', lambda x: x))
    robot.behavior = mySM
    robot.behavior.start(traceTasks=robot.gfx.tasks())


def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())


def brainStop():
    pass
