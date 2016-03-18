# Problem 1
# i) variable b refers to the same object as variable a
# ii) variable c points to a new object with all elements copied from the corresponding elements
# of variable a with the exception of the nested list, which refers to the same nested list that
# variable a points to.
# iii) variable d points to a new object, where every element is a new copy of the corresponding
# element of variable a, including the nested list. All elements in variable d point to different
# objects that the elements in variable a point to.

# Problem 2
# The problem is that the variables leftObstacle and rightObstacle are never updated within the
# while loop block of code, so they will remain as their initial values (i.e. will never move,
# or will not stop moving)

# Problem 3
def comp(x):
    return x ** 3 + 4 * x ** 2 + 6 * x + 1


# Problem 4
def genList(n1, n2):
    mylist = []
    for i in range(n1, n2 + 1):  # Yes I know there's a better way to do it.
        if i % 3 == 0:
            mylist.append(i)
    return mylist


# Problem 5
def matAdd(A, B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C


A = [[1, 2, 3], [4, 5, 6]]
B = [[10, 20, 30], [40, 50, 60]]
print matAdd(A, B)

# Problem 6
f = open("C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\MidTerms\TextFileMidTerm2015\data1.txt")


def getSchedule(f):
    info = f.readlines()
    dictionary = {}
    everything = []
    for i in info:
        everything += i.split()
    for i in range(len(everything)):
        day_list = []
        if len(everything[i]) > 2:
            hi = everything[i + 1:]
            for j in range(0, len(hi), 2):
                if len(hi[j]) <= 2:
                    meow = (int(hi[j]), int(hi[j + 1]))
                    day_list.append(meow)
                else:
                    break
            dictionary[everything[i]] = day_list
    return dictionary


def dictSchedule(f):
    dictionary = {}
    for key, value in getSchedule(f).iteritems():
        summa = 0
        for i in range(len(value)):
            summa += value[i][1] - value[i][0]
        dictionary[key] = summa
    return dictionary

def comparesched(tup1,tup2):
    if tup2[0]<tup1[0]<tup2[1] or tup2[0]<tup1[1]<tup2[1]:
        return True
    return False

def findConflict(dictionarySchedule):
    Boo = {}
    for i in dictionarySchedule:
        Boo[i] = False
        for j in range(len(dictionarySchedule[i])):
            for k in range(len(dictionarySchedule[i])):
                if comparesched(dictionarySchedule[i][j][k],dictionarySchedule[i][j][k-1]):
                    Boo[i] = True
                    break
            break
    return Boo

            # a = dictionarySchedule[i][j]
            # b = dictionarySchedule[i][j-1]
            # if b[0] < a[0] < b[1]:
            #     Boo[i] = True
            #     break
            # elif b[0] < a[1] < b[1]:
            #     Boo[i] = True
            #     break
    return Boo

thedict = getSchedule(f)
print thedict
print findConflict(thedict)
