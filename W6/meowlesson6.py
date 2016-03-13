#Cohort problems
import math
import string
#Problem 1
def reverse(meow):
    return meow[::-1]

# print reverse('hi')

#Problem 2
def isValidPassword(password):
    numbercount = 0
    acceptable = []
    for i in range(48,58):
        acceptable.append(i)
    for i in range(65,91):
        acceptable.append(i)
    for i in range(97,123):
        acceptable.append(i)
    for letter in password:
        if ord(letter) not in acceptable:
            return False
        elif ord(letter) in range(48,58):
            numbercount += 1
    if len(password) < 8:
        return False
    elif numbercount < 2:
        return False
    else:
        return True

# print isValidPassword('test')
# print isValidPassword('testtest')
# print isValidPassword('testt22')
# print isValidPassword('testte22')

#Problem 3
def prefix(s1,s2):
    a = min(len(s1),len(s2))
    if len(s1) <= len(s2):
        if s1 != s2[:a]:
            return prefix(s1[:-1],s2[:a-1])
        else:
            return s1
    else:
        if s2 != s1[:a]:
            return prefix(s1[:a-1],s2[:-1])
        else:
            return s2

# ans = prefix('disinfection','distance')
# print ans
# ans = prefix('testing','technical')
# print ans
# ans = prefix('drinking','drinker')
# print ans
# ans = prefix('rosses','crosses')
# print ans
# ans = prefix('distancetion','distance')
# print ans

#Problem 4
#for windows: add  to file name
file = open('C:\\Users\\HanWei\\Dropbox\\SUTDNotes\\SUTDTerm3\\DigitalWorld\\W6\\xy.dat','r')
def read2columns(f):
    class Coordinate:
        x = 1
        y = 1
    themax = Coordinate()
    themin = Coordinate()
    maxx, maxy, minx, miny = None,None,None,None
    for line in f:
        x,y = line.split()
        x,y = float(x),float(y)
        magnitude = math.sqrt((x**2)+(y**2))
        if maxx == None:
            maxx,maxy,minx,miny = x,y,x,y
            print 'max is ', maxx,maxy, 'min is ', minx,miny
        elif magnitude > math.sqrt(maxx**2 + maxy**2):
            maxx,maxy = x,y
        elif magnitude < math.sqrt(minx**2 + miny**2):
            minx,miny = x,y
    themax.x,themax.y,themin.x,themin.y = maxx,maxy,minx,miny
    return themax,themin
    # for item in f:
    #     value = Coordinate
    #     value.x,value.y = item.strip().split()
    #     value.x,value.y = float(value.x),float(value.y)
    #     mag = math.sqrt(value.x**+value.y**2)
    #     magnitudes += mag

pmax,pmin = read2columns(file)
print 'max: (%f, %f)'%(pmax.x,pmax.y)
print 'min: (%f, %f)'%(pmin.x,pmin.y)


#Problem 5
def replace(f, oldS, newS):
    return f.read().replace(oldS,newS)
    # newtext = ''
    # for line in f:
    #     newtext += line.replace(oldS,newS)
    # return newtext
ruff = open('C:\\Users\\HanWei\\Dropbox\\SUTDNotes\\SUTDTerm3\\DigitalWorld\\W6\\replace.txt','r')
meow = replace(ruff,'the','MEOW')
print meow

#Homework
#Problem 1
def binaryToDecimal(thebin):
    total = 0
    current = int(thebin)
    for each in range(len(thebin)):
        total += int(thebin[len(thebin)-1-each])*2**(each)
        current = current/10
    return total

print binaryToDecimal('100')
# print binaryToDecimal('101')
# print binaryToDecimal('10001')
# print binaryToDecimal('10101')

#Problem 2
def uncompressed(s):
    uncomp = ''
    for letter in range(0,len(s),2):
        uncomp += int(s[letter])* s[letter+1]
    return uncomp

print uncompressed('2a5b1c')

#Problem 3
UpperCase = string.ascii_uppercase

def getBaseCounts2(dna):
    count = {'A':0,'T':0,'C':0,'G':0}
    for i in dna:
        if i in 'ACTG':
            count[i] += 1
        elif i not in UpperCase:
            return 'The input DNA string is invalid'
    return count

print getBaseCounts2('ATGCTATTCaA')
# def getBaseCounts(dna):
#     count = {}
#     for i in dna:
#         if i in 'ACTG':
#             if i in count:
#                 count[i] = count[i] + 1
#             else:
#                 count[i] = 1
#         else:
#             return 'The input DNA string is invalid'
#     return count

#Problem 4
thefile = open('constants.txt','r')
def fundamentalConstants(f):
    constants = {}
    lines = f.readlines()
    for i in range(len(lines)):
        if i in [1,0]:
            pass
        else:
            line1 = lines[i].split()
            constants[line1[0]] = float(line1[1])
    return constants

print fundamentalConstants(thefile)


#Problem 5
def scores(f):
    total = 0
    whole = f.read().split()
    for each in range(len(whole)):
        total += float(whole[each])
    average = total/len(whole)
    return total,average