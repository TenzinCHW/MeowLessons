# Final boss!!

from libdw import sm
from binascii import a2b_uu


# Part B

# Question 3

def maxOccurrences(inp):
    inplist = inp.split()
    countingdict = {}
    for i in inplist:
        if int(i) in countingdict:
            countingdict[int(i)] += 1
        else:
            countingdict[int(i)] = 1
    maxoccur = []
    occur = 0
    for key, val in countingdict.iteritems():
        if val > occur:
            maxoccur = [key]
            occur = val
        elif val == occur:
            maxoccur.append(key)
    return sorted(maxoccur), occur


# inp = '2 3 40 3 5 4 -3 3 3 2 0'
# print maxOccurrences(inp)
#
# inp = '9 30 3 9 3 2 4'
# print maxOccurrences(inp)

# Question 4
def binaryconverter(somestr):
    if somestr == 0:
        ans = '000'
    elif somestr == 1:
        ans = '001'
    elif somestr == 2:
        ans = '010'
    elif somestr == 3:
        ans = '011'
    elif somestr == 4:
        ans = '100'
    elif somestr == 5:
        ans = '101'
    elif somestr == 6:
        ans = '110'
    elif somestr == 7:
        ans = '111'
    return ans


class RingCounter(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        if inp == 1:
            nextstate = 0
        elif inp == 0:
            if state < 7:
                nextstate = state + 1
            elif state == 7:
                nextstate = 0
        out = binaryconverter(nextstate)
        return nextstate, out


# meow = RingCounter()
# print meow.transduce([0,0,0,0,0,0,0,0,0])
# meow = RingCounter()
# print meow.transduce([0,0,0,1,0,0,0,0,0])
# meow = RingCounter()
# print meow.transduce([0,0,0,1,0,0,1,0,0])

# Question 5

class Avatar:
    def __init__(self, name, hp=100, position=(1, 1)):
        self.name = name
        self.hp = hp
        self.position = position

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getHP(self):
        return self.hp

    def setHP(self, hp):
        self.hp = hp

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def heal(self, healamt=1):
        if healamt < 0:
            pass
        else:
            self.hp += healamt

    def attacked(self, attackpower=-1):
        if attackpower > 0:
            pass
        else:
            self.hp += attackpower


# a = Avatar('John')
# print (a.name, a.hp, a.position)
# a = Avatar('Jane', 150, (10, 10))
# print (a.name, a.hp, a.position)
# a = Avatar('John')
# a.setName('Jude')
# print a.getName()
# a = Avatar('John')
# a.setPosition((1, 3))
# a.setHP(200)
# print a.getPosition()
# print a.getHP()
# a = Avatar('John')
# a.heal(5)
# print a.getHP()
# a = Avatar('John')
# a.attacked(20)
# print a.getHP()
# a = Avatar('John')
# a.heal()
# print a.getHP()
# a = Avatar('John')
# a.attacked()
# print a.getHP()
# a = Avatar('John')
# a.attacked(2)
# a.heal(-2)
# print a.getHP()

# Question 6
import copy


class Map:
    def __init__(self, worldinfo):
        self.world = copy.deepcopy(worldinfo)

    def whatIsAt(self, position):
        if position not in self.world:
            thingthere = 'Empty'
        else:
            thing = self.world[position]
            if thing == 'x':
                thingthere = 'Exit'
            elif thing == 0:
                thingthere = 'Wall'
            elif thing > 0:
                thingthere = 'Food'
            elif thing < 0:
                thingthere = 'Enemy'
        return thingthere

    def getEnemyAttack(self,pos):
        if self.whatIsAt(pos) != 'Enemy' or pos not in self.world:
            return False
        else:
            return self.world[pos]

    def getFoodEnergy(self,pos):
        if self.whatIsAt(pos) != 'Food' or pos not in self.world:
            return False
        else:
            return self.world[pos]

    def removeEnemy(self,pos):
        if self.whatIsAt(pos) != 'Enemy' or pos not in self.world:
            return False
        else:
            del self.world[pos]
            return True

    def eatFood(self,pos):
        if self.whatIsAt(pos) != 'Food' or pos not in self.world:
            return False
        else:
            del self.world[pos]
            return True

    def getExitPosition(self):
        for key, value in self.world.iteritems():
            if value is 'x':
                return key

    def getSearchMap(self):
        newmap = {}
        for i in range(6):
            for j in range(6):




# world = {(0,0):0,(1,0):0,(2,0):0,(3,0):0,(4,0):0,(5,0):0,(0,1):0,(1,1):2,(2,1):-3,(5,1):0,(0,2):0,(5,2):0,(0,3):0,(5,3):0,(0,4):0,(5,4):0,(0,5):0,(1,5):0,(2,5):0,(3,5):0,(4,5):'x',(5,5):0}
# m = Map(world)
# print m.world
# print m.whatIsAt((1,0))
# print m.whatIsAt((2,1))
# print m.whatIsAt((1,1))
#
# w1 = m.getFoodEnergy((1,1))
# w2 = m.getFoodEnergy((3,3))
# print (w1,w2)
#
# w1,w2 = m.getEnemyAttack((2,1)),m.getEnemyAttack((3,3))
# print (w1,w2)
#
# w1,w2,w3 = m.getEnemyAttack((2,1)),m.removeEnemy((2,1)),m.getEnemyAttack((2,1))
# print (w1,w2,w3)
#
# print m.whatIsAt((1,4))
# print m.getFoodEnergy((1,4))
# print m.getEnemyAttack((1,4))
# print m.whatIsAt((4,5))
# print m.getExitPosition()
# print m.world is world

class DW2Game(sm.SM):
    def __init__(self, avatar, lemap):
        startState = (avatar,copy.deepcopy((lemap)))

    def nextpos(self,pos,dir):
        x = None
        y = None
        if dir == 'up':
            x,y = pos[0],pos[1] + 1
        elif dir == 'down':
            x,y = pos[0],pos[1] -1
        elif dir == 'left':
            x,y = pos[0] - 1,pos[1]
        elif dir == 'right':
            x,y = pos[0]+1,pos[1]
        if x <0:
            x=0
        if y < 0:
            y = 0
        newpos = (x,y)
        return newpos

    def getNextValues(self, state, inp):
        newpos = self.nextpos(state[0].getPosition(),inp[1])
        if inp[0] == 'move':
            if state[1].whatIsAt(newpos) != 'Wall' and state[1].whatIsAt(newpos) != 'Enemy':
                theavatar = state[0].setPosition(newpos)
            if state[1].whatIsAt(newpos) == 'Food':
                theavatar = state[0].heal(state[1][newpos])
                lemap = state[1].eatFood(newpos)
            else:
                theavatar = state[0]
                lemap = state[1]
        if inp[0] == 'attack':
            if state[1].whatIsAt(newpos) != 'Enemy':
                theavatar = state[0]
                lemap = state[1]
            else:
                theavatar = state[0].attacked(state[1][newpos])
                lemap = state[1].removeEnemy(newpos)
        return ((theavatar,lemap),(theavatar,newpos,avatarhp))

    def done(self, state):
        if state[1][state[0].getPosition] == 'x':
            return True
        else:
            return False
## THIS QN WRONG ALR. Forgot the done function T_T

# Question 8
