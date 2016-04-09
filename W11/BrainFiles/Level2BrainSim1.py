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

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.65  # Yes I know I should have made these class attributes... It was late and I was tired.
desiredFront = 0.5
forwardVelocity = 0.08
timer1 = 0
timer2 = 0
waitflag = False
checked = False
turned = False
stopped = False
medianlist = [[], [], [], [], [], []]
url = "https://2dtest2016.firebaseio.com/"  # URL to Firebase
token = "CUOhY38xTvnYarBkqQis7H7UzRYbMoEwEyEei07P"
firebase = firebase.FirebaseApplication(url, token)
req = urllib2.Request('http://people.sutd.edu.sg/~oka_kurniawan/y2016t3/2d/l2s4.inp')
req.add_header('User-agent', 'SUTD 2D Demo')
res = urllib2.urlopen(req)

destination = []
for line in res:
    destination.append(line.strip())


def pathplanner(instructions):  # Turned network into tree by ignoring one node
    timestovisit = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    path = ['Straight', 'Straight', 'X']
    for i in instructions:
        timestovisit[i[0]] = int(math.ceil(int(i[1:]) / 6.0))
    for key, value in timestovisit.iteritems():
        if key == 'A':
            for each in range(value):
                path.append('Right'), path.append('Right'), path.append(key), path.append('Left'), path.append(
                    'Left'), path.append('X')
        elif key == 'B':
            for each in range(value):
                path.append('Right'), path.append('Straight'), path.append(key), path.append('Straight'), path.append(
                    'Left'), path.append('X')
        elif key == 'C':
            for each in range(value):
                path.append('Right'), path.append('Left'), path.append('Right'), path.append(key), path.append(
                    'Left'), path.append('Right'), path.append('Left'), path.append('X')
        elif key == 'D':
            for each in range(value):
                path.append('Right'), path.append('Left'), path.append('Straight'), path.append(key), path.append(
                    'Straight'), path.append('Right'), path.append('Left'), path.append('X')
    return path


# Possible position/area: 'Corridor','Junction'
class BadBoy(sm.SM):
    startState = [0, 'Corridor', 0, pathplanner(destination),
                  None, ]  # [error for following wall, position/area, number of plates (haha I thought we had to keep
    # track of these), instructions, desiredtheta]

    def done(self, state):  # When to stop
        if len(state[3]) == 0:  # No more instructions to carry out
            return True
        return False

    def getNextValues(self, state, inp):
        global mytime, checked, timer, k1, k2, turned, stopped, medianlist
        theta, temp, ldr = inp.odometry.theta, inp.temperature, inp.light
        print state
        print theta

        for i in range(6):  # Moving median code to minimize erroneous readings from sonnars
            medianlist[i].append(inp.sonars[:6][i])
            if len(medianlist[i]) > 6:
                del medianlist[i][0]

        if len(medianlist[0]) < 6:  # Do not do anything until we have 6 values stored for averaging.
            return state, io.Action(fvel=0, rvel=0)
        else:  # Assign the medians of each list to variables
            left, fleft, front, fright, right, back = sorted(medianlist[0])[2], sorted(medianlist[1])[2], \
                                                      sorted(medianlist[2])[2], sorted(medianlist[3])[2], \
                                                      sorted(medianlist[4])[2], sorted(medianlist[5])[2]

        print "Left: ", left, "Fleft: ", fleft, "Front: ", front, "Fright: ", fright, "Right: ", right, "Back: ", back

        if state[1] == 'Corridor':  # Checks if ebot is supposed to be in a corridor
            if state[3][0] in 'ABCDX':  # Checks if it is in a station.
                print "Going into station"
                if front <= 1 and not stopped:  # Checks if ebot has stopped, and stops it if it is less than or 1m
                    #  away from wall (in simulator)
                    return stopper(state)
                elif front > 0.5 and not stopped and not checked and not turned:  # Follows wall until above cases are
                    #  fulfilled
                    return followwall(state, front, fleft, fright, left, right, theta)
                elif stopped and not turned:  # checks if it has turned, if not, then makes it do a U-turn
                    return uturn(state, theta)
                elif stopped and turned and not checked:  # Checks if upload and file write has been made
                    return uploadwrite(state, inp.sonars[:6], temp, ldr)
                else:  # If none of above hold true, ebot has completed all tasks at station. Reset all variables for
                    #  next station
                    checked = False
                    turned = False
                    stopped = False
                    del state[3][0]
                    return followwall(state, front, fleft, fright, left, right, theta)  # Continue following wall
            elif left > 1.4 or right > 1.4 or fleft > 1.4 or fright > 1.4:  # If straightening of ebot inside the
                #  corridor has gone well, a spike in one of the side readings means that the ebot has entered a junction.
                state[1] = 'Junction'
                state[0] = 0
                print "Changing to junction"
                return state, io.Action(fvel=0.1, rvel=0)
            else:  # Just follow the wwall if there isn't anything fun happening.
                print 'Following walls'
                return followwall(state, front, fleft, fright, left, right, theta)

        elif state[1] == 'Junction':  # Checks if the ebot should be in a junction
            if state[3][0] == 'Straight':  # Checks if the instruction for this junction is to go straight
                if fleft < 1.5 and fright < 1.5 and left < 1.4 and right < 1.4:
                    state[1] = 'Corridor'
                    del state[3][0]
                    state[0] = 0
                    print "Changing to corridor"
                    return state, io.Action(fvel=0.1, rvel=0)  # Cannot make the velocities 0
                elif (fleft < 0.6 or fright < 0.6 or left < 0.5 or right < 0.5):
                    return followwall(state, front, fleft, fright, left, right,
                                      theta)  # todo - calibrate rvel for real ebot
                else:
                    print "Going straight"
                    return state, io.Action(fvel=0.1, rvel=0)

            elif state[3][0] == 'Right' or state[3][0] == 'Left':  # Calculate angle to rotate to if the instruction at
                # this junction is to turn
                if state[4] == None:  # Makes sure that there isn't a currently stored value of desiredtheta, otherwise
                    # only the parts after this will be executed i.e. turning to until odometry theta is near
                    # desiredtheta
                    if state[3][0] == 'Right':
                        state[4] = theta - (math.pi / 2)  # Assuming that ebot starts facing X from S, the value of
                        # desiredtheta to turn to will be the current angle subtract 90 degrees
                    elif state[3][0] == 'Left':
                        state[4] = theta + (
                            math.pi / 2)  # Otherwise the value of desiredtheta will be current angle add
                        # 90 degrees
                desiredtheta = state[
                    4]  # Assigns the value that is being held in the state desiredtheta to the variable
                # name desiredtheta
                if desiredtheta > 2 * math.pi:  # Corrects for values over 2 * pi
                    desiredtheta = round(desiredtheta - 2 * math.pi, 2)
                elif desiredtheta < 0:  # Corrects for values under 0. Odometry theta returns a value from 0 to 2 * pi
                    desiredtheta = round(desiredtheta + 2 * math.pi, 2)
                if state[3][0] == 'Right':  # Turn right until the value of odometry theta is near the value of
                    # desiredtheta
                    if 0.2 < abs(theta - desiredtheta):
                        print "Turning right"
                        print desiredtheta
                        fevel, revel = 0.1, -0.07
                    else:  # Transition back into corridor state if the value of odometry theta is near enough to the
                        # value of desiredtheta
                        state[1] = 'Corridor'
                        del state[3][0]
                        state[0], state[4], fevel, revel = 0, None, 0.1, 0
                        print "Changing to corridor"
                    return state, io.Action(fvel=fevel, rvel=revel)  # todo - calibrate rvel for real ebot
                elif state[3][0] == 'Left':
                    if 0.2 < abs(
                                    desiredtheta - theta):  # Turn left until the value of odometry theta is near the value of
                        # desiredtheta, resets all states associated with junction state
                        print "Turning left"
                        print desiredtheta
                        fevel, revel = 0.1, 0.07
                    else:  # Transition back into corridor state if the value of odometry theta is near enough to the
                        # value of desiredtheta, resets all states associated with junction state
                        state[1] = 'Corridor'
                        print "Changing to corridor"
                        del state[3][0]
                        state[0], state[4], fevel, revel = 0, None, 0.1, 0.025
                    return state, io.Action(fvel=fevel, rvel=revel)
                else:  # There is some unknown state. Move forward to try to activate a different state.
                    print state[3][0]
                    return state, io.Action(fvel=0.1, rvel=0)


def followwall(state, Front, FLeft, FRight, Left, Right, Theta):  # Wallfollower function
    if FLeft >= 1.3 or FRight >= 1.3:  # Use the sides otherwise if the front diagonal sensors detect a junction
        k1 = 23
        k2 = -22.88
        revel = k1 * (Left - Right) + k2 * state[0]
        state[0] = Left - Right
        print "Using side to straighten"
        return state, io.Action(fvel=forwardVelocity, rvel=revel)

    else:  # Use front diagonal sensors otherwise
        k1, k2 = 23, -22.9
        revel = k1 * (FLeft - FRight) + k2 * state[0]
        state[0] = FLeft - FRight
        return state, io.Action(fvel=forwardVelocity, rvel=revel)


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




def stopper(state):  # Stop the ebot
    global stopped, timer1, timer2, waitflag
    if not waitflag:  # Starts the waitflag to tell the ebot to start waiting
        timer1 = time()
        waitflag = True
    elif waitflag:
        timer2 = time()
        if timer2 - timer1 >= 8:  # Waits until the ebot has waited for 8 seconds, sets global variables for next
            # function
            stopped = True
            waitflag = True
    return state, io.Action(fvel=0, rvel=0)  # Just keep waiting, just keep waiting, just keep waiting, waiting and
    #  waiting


def uploadwrite(state, sonars, temp, ldr):  # Writes the time that the station was reached, ldr reading, and
    # temperature reading into file, and uploads it onto firebase
    global checked
    fin = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\\2D\DW2DShenanigans.txt', 'a+')  # Opens file for appending
    now = datetime.now().strftime('%H:%M:%S') + '|' + datetime.now().strftime('%d/%m/%Y')  # Str format of time for
    # firebase upload
    othernow = datetime.now().strftime('<%H:%M:%S>') + '||' + datetime.now().strftime('<%d/%m/%Y>' + '||')  # Str format
    #  of time for file write
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
    else:  # Should never enter this state
        print 'Not a station'
    checked = True  # Sets checked flag to true so ebot can continue moving
    fin.close()  # Closes the file
    return state, io.Action(fvel=0, rvel=0)  # Don't move while you do everything in this function


def uturn(state, theta):  # Turn ebot 180 degrees
    global turned
    thetadict = {'A': math.pi, 'B': 3 * math.pi / 2, 'C': 3 * math.pi / 2, 'D': 0, 'X': math.pi}  # THIS IS FOR LEVEL 2
    # It states the value that odometry theta should be after the ebot turns from facing wall
    error = abs(thetadict[state[3][0]] - theta) # Difference between the required theta as above and odometry theta
    if error > 0.05: # If error is too big, keep turning
        fevel = 0
        revel = 0.15
    else: # Otherwise, stop turning
        turned = True
        fevel = 0
        revel = 0
    return state, io.Action(fvel=fevel, rvel=revel)


mySM = BadBoy()


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
