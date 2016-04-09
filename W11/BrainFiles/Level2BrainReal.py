import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist
from time import time
from datetime import datetime
import firebase
import urllib2
from libdw.replanner import *

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.65
desiredFront = 0.5
forwardVelocity = 0.08
timer1 = 0
timer2 = 0
waitflag = False
checked = False
turned = False
stopped = False
medianlist= [[],[],[],[],[],[]]
url = "https://flickering-fire-1661.firebaseio.com/"  # URL to Firebase
token = "ZpSWTZaRaODNivf2S3Vil0a50BAPjx1ZhGsVbL2S"
firebase = firebase.FirebaseApplication(url, token)
req = urllib2.Request('http://people.sutd.edu.sg/~oka_kurniawan/y2016t3/2d/l2s4.inp')
req.add_header('User-agent', 'SUTD 2D Demo')
res = urllib2.urlopen(req)

destination = []
for line in res:
    destination.append(line.strip())

def pathplanner(instructions):
    timestovisit = {'A':0,'B':0,'C':0,'D':0}
    path = ['Straight','Straight','X']
    for i in instructions:
        timestovisit[i[0]] = int(math.ceil(int(i[1:])/6.0))
    for key,value in timestovisit.iteritems():
        if key == 'A':
            for each in range(value):
                path.append('Right'), path.append('Right'), path.append(key), path.append('Left'),path.append('Left'),path.append('X')
        elif key == 'B':
            for each in range(value):
                path.append('Right'),path.append('Straight'),path.append(key),path.append('Straight'),path.append('Left'),path.append('X')
        elif key == 'C':
            for each in range(value):
                path.append('Right'),path.append('Left'),path.append('Right'),path.append(key),path.append('Left'),path.append('Right'),path.append('Left'),path.append('X')
        elif key == 'D':
            for each in range(value):
                path.append('Right'),path.append('Left'),path.append('Straight'),path.append(key),path.append('Straight'),path.append('Right'),path.append('Left'),path.append('X')
    return path


# Possible position/area: 'Corridor','Junction'
class WallFollower(sm.SM):
    startState = [0, 'Corridor', 0, pathplanner(destination), None, ]  # [error for following wall, position/area, number of plates, instructions, desiredtheta <<please create this before running]

    def done(self, state):
        if len(state[3]) == 0:
            return True
        return False

    def getNextValues(self, state, inp):
        global mytime, checked, timer, k1, k2, turned, stopped, medianlist
        theta, temp, ldr = inp.odometry.theta, inp.temperature, inp.light
        print state
        print theta

        for i in range(6):
            medianlist[i].append(inp.sonars[:6][i])
            if len(medianlist[i])>6:
                del medianlist[i][0]

        if len(medianlist[0])<6:
            return state, io.Action(fvel=0,rvel=0)
        else:
            left, fleft, front, fright, right, back = sorted(medianlist[0])[2], sorted(medianlist[1])[2],sorted(medianlist[2])[2],sorted(medianlist[3])[2],sorted(medianlist[4])[2],sorted(medianlist[5])[2]

        print "Left: ", left, "Fleft: ", fleft, "Front: ", front, "Fright: ", fright, "Right: ", right, "Back: ", back

        if state[1] == 'Corridor':
            if state[3][0] in 'ABCDX':
                print "Going into station"
                if front <= 0.8 and not stopped:
                    return stopper(state)
                elif front > 0.5 and not stopped and not checked and not turned:
                    return followwall(state, front, fleft, fright, left, right, theta)
                elif stopped and not turned:
                    return uturn(state, theta)
                elif stopped and turned and not checked:
                    return uploadwrite(state, inp.sonars[:6], theta, temp, ldr)
                else:
                    checked = False
                    turned = False
                    stopped = False
                    del state[3][0]
                    return followwall(state, front, fleft, fright, left, right, theta)
            # elif ((right> 1.2 and fright > 1.2) or (left > 1.2 and fleft > 1.2)) and (back > 1.3 and front > 1.3):
            elif left > 1.4 or right > 1.4 or fleft>1.4 or fright>1.4:
                state[1] = 'Junction'
                state[0] = 0
                print "Changing to junction"
                return state, io.Action(fvel=0.1, rvel=-0.02858)
            # elif left > 0.8 or right > 0.8:
            #     return followwall(state, fleft, fright, left, right)
            # elif fleft>1.3 or fright > 1.3:
            #     if (state[3][0] == 'Left' or state[3][0] == 'Right') and back > 1.3:
            #         print "Changing to junction"
            #         state[1] = 'Junction'
            #         state[0] = 0
            #     return state,io.Action(fvel=0.1,rvel=-0.02858)
            else:
                print 'Following walls'
                return followwall(state, front, fleft, fright, left, right, theta)

        elif state[1] == 'Junction':
            if state[3][0] == 'Straight':
                if fleft < 1.5 and fright < 1.5 and left < 1.4 and right < 1.4:
                    state[1] = 'Corridor'
                    del state[3][0]
                    state[0] = 0
                    print "Changing to corridor"
                    return state, io.Action(fvel=0.1, rvel=0)  # Cannot make the velocities 0
                elif (fleft <0.6 or fright < 0.6 or left < 0.5 or right < 0.5):
                    return followwall(state,front,fleft,fright,left,right,theta)
                else:
                    print "Going straight"
                    return state,io.Action(fvel=0.1,rvel=-0.02858)

            elif state[3][0] == 'Right' or state[3][0] == 'Left':
                if state[4] == None:
                    if state[3][0] == 'Right':
                        state[4] = theta - (math.pi / 2 + 0.3)
                    elif state[3][0] == 'Left':
                        state[4] = theta + (math.pi / 2 - 0.3)
                desiredtheta = state[4]
                if desiredtheta > 2 * math.pi:
                    desiredtheta = round(desiredtheta-6.2,2)
                elif desiredtheta < 0:
                    desiredtheta = round(desiredtheta+6.2,2)
                if state[3][0] == 'Right':
                    if 0.2 < abs(theta - desiredtheta):
                        print "Turning right"
                        print desiredtheta
                        fevel, revel = 0.05, -0.08
                    else:
                        state[1] = 'Corridor'
                        del state[3][0]
                        state[0], state[4], fevel, revel = 0, None, 0.1, -0.02858
                        print "Changing to corridor"
                    return state, io.Action(fvel=fevel, rvel=revel)  # todo - calibrate rvel for real ebot
                elif state[3][0] == 'Left':
                    if 0.2 < abs(desiredtheta - theta):
                        print "Turning left"
                        print desiredtheta
                        fevel, revel = 0.05, 0.08
                    else:
                        state[1] = 'Corridor'
                        print "Changing to corridor"
                        del state[3][0]
                        state[0], state[4], fevel, revel = 0, None, 0.1, 0.025
                    return state, io.Action(fvel=fevel, rvel=revel)  # todo - calibrate rvel for real ebot
                else:
                    print state[3][0]
                    return state, io.Action(fvel=0.1, rvel=-0.02858)


def followwall(state, Front, FLeft, FRight, Left, Right, Theta):
    # desiredtheta = (Theta // (math.pi/2) ) * math.pi/2 #todo might need a diff way to estimate desiredtheta
    # if Front < 1.31:
    #     desiredtheta += math.pi/2
    # if desiredtheta > 2*  math.pi:
    #     desiredtheta -= 2*math.pi
    # elif desiredtheta < 0:
    #     desiredtheta += 2*math.pi
    # if abs(desiredtheta-Theta) > 0.4:
    # k1 = 0.13
    # k2 = -0.1
    # revel = k1 * (desiredtheta - Theta) + k2 * state[0]
    # state[0] = desiredtheta - Theta
    # print 'Using theta to control dir'
    # return (state, io.Action(fvel=forwardVelocity, rvel=revel))
    # if FLeft <= 1.3 or FRight <=1.3:
    #     k1 = 23
    #     k2 = -22.9
    #     revel = k1 * (FLeft - FRight) + k2 * state[0]
    #     state[0] = FLeft - FRight
    #     print "Using front to straighten"
    #     return state, io.Action(fvel=0.08, rvel=revel)

    if FLeft >= 1.3 or FRight >= 1.3:
        k1 = 23
        k2 = -22.88
        if FLeft >= 1.3 and not FRight >= 1.3:
            revel = k1*(0.6-Right) + k2*state[0]
            return state,io.Action(fvel=forwardVelocity,rvel=revel)
        elif FRight >= 1.3 and not FLeft >= 1.3:
            revel = k1*(0.6-Left) + k2*state[0]
            return state,io.Action(fvel=forwardVelocity,rvel=revel)
        revel = k1 * (0.6-Left) + k2 * state[0]
        state[0] = Left - Right
        print "Using side to straighten"
        return state, io.Action(fvel=forwardVelocity, rvel=revel)
    else:
        k1,k2= 23,-22.9
        revel = k1 * (FLeft - FRight) + k2*state[0]
        state[0] = FLeft - FRight
        return state,io.Action(fvel=forwardVelocity,rvel=revel)




def stopper(state):
    global stopped, timer1,timer2,waitflag
    if not waitflag:
        timer1 = time()
        waitflag = True
        return state,io.Action(fvel=0,rvel=0)
    elif waitflag:
        timer2 = time()
        if timer2 - timer1 >=8:
            stopped = True
            waitflag = True
    return state, io.Action(fvel=0,rvel=0)


def uploadwrite(state, sonars, theta, temp, ldr):
    fin = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\\2D\DW2DShenanigans.txt', 'a+')
    now = datetime.now().strftime('%H:%M:%S') + '|' + datetime.now().strftime('%d/%m/%Y')
    othernow = datetime.now().strftime('<%H:%M:%S>') + '||' + datetime.now().strftime('<%d/%m/%Y>' + '||')
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
    thetadict = {'A': math.pi, 'B': 3*math.pi / 2, 'C': 3*math.pi / 2, 'D': 0, 'X': math.pi}  # THIS IS FOR LEVEL 2
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


mySM = WallFollower()


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
