# Question 3
import cmath
import math
import copy


def norm(z1, z2, z3):
    return round(cmath.sqrt(z1 * z1.conjugate() + z2 * z2.conjugate() + z3 * z3.conjugate()).real, 3)


# z1 = 1 + 3j
# z2 = -1 + 3j
# z3 = -1 - 3j
# print norm(z1, z2, z3)
# z1 = 1 + 2j
# z2 = 1 + 2j
# z3 = - 1 - 2j
# print norm(z1, z2, z3)
# z1 = 1 + 1j
# z2 = -1 + 1j
# z3 = - 1 - 1j
# print norm(z1, z2, z3)


# Question 4

def factors(n):
    allfactors = []
    for i in range(1, n + 1):
        if n % i == 0:
            allfactors.append(i)
    return allfactors


# print factors(6)
# print factors(12)
# print factors(7)
# print factors(15)
# print factors(21)
# print factors(1)
# print factors(9)

# Question  5

def combinations(n1, n2):
    a = sorted([n1, n2])
    count = 0
    combi = []
    for i in range(a[0], a[1] + 1):
        for j in range(a[0], a[1] + 1):
            if i != j and i < j:
                combi.append((i, j))
                count += 1
    return combi, count


# print combinations(1,7)
# print combinations(3,5)
# print combinations(-1,2)
# print combinations(0,0)

# Question 6a
# f = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\MidTerms\TextFileMidTerm2015\gauss2.txt', 'r')


def readMatrix(f):
    Matrix = {'matrix': [], 'op': []}
    thekey = 'matrix'
    for line in f:
        if line.strip().isalpha():
            if line.strip() == 'OP':
                thekey = 'op'
        else:
            elements = line.strip().split()
            theelements = []
            if thekey == 'op':
                # print elements
                Matrix[thekey].append(elements)
                if [] in Matrix[thekey]:
                    Matrix[thekey].remove([])
            else:
                for element in elements:
                    theelements.append(float(element))
            Matrix[thekey].append(theelements)
    if [] in Matrix[thekey]:
        Matrix[thekey].remove([])
    print Matrix
    return Matrix


# print readMatrix(f)
# a = f.readlines()
# print a

# Question 6b

def mulRowByC(matA, i, c):
    result = matA[:]
    newrow = []
    for element in matA[i]:
        newrow.append(element * c)
    result[i] = newrow
    return result


# A = [[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
# print mulRowByC(A,0,2)

# Question 6c

def addRowMulByC(matA, i, c, j):
    oldMat = mulRowByC(matA, i, c)
    newMat = matA[:]
    newrow = []
    for element in range(len(oldMat[j])):
        newrow.append(oldMat[j][element] + oldMat[i][element])
    newMat[j] = newrow
    return newMat


# A = [[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
# print addRowMulByC(A,0,0.5,1)

# Question 6d
# I did not finish this question in the exam. Didn't understand what 'op' in the dictionary was.
# But I think I fixed it now :D
def gaussElimination(data):
    newMatrix = data['matrix'][:]  # Apparently I don't even need to deepcopy the matrix
    for eachrow in data['op']:  # Loop over each list in the list assigned to key 'op' in dictionary called data
        if eachrow[0] == '1':  # If the first element of that list is '1'
            newMatrix = mulRowByC(newMatrix, int(eachrow[1]), float(eachrow[2]))  # Call mulRowByC,
            # passing in as arguments whatever newMatrix is now and the remaining elements of the list,
            # and assign it to newMatrix
        elif eachrow[0] == '2':  # Else if first element of the list is '2',
            newMatrix = addRowMulByC(newMatrix, int(eachrow[1]), float(eachrow[2]), int(eachrow[3]))
            # Call addRowMulByC, passing in arguments whatever newMatrix is right now and the remaining
            # elements of the list, and assign it to newMatrix
    return data['matrix'], newMatrix  # The question asked me to return the old and new matrices in a tuple.


# f = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\MidTerms\TextFileMidTerm2015\gauss1.txt', 'r')
# print gaussElimination(readMatrix(f))


# Question 7
# Got this one wrong :( Haven't fixed it yet
def maxProductThree(num):
    allproducts = []
    for i in range(len(num)):
        for j in range(len(num)):
            for k in range(len(num)):
                if i != j and i != k and j != k:
                    allproducts.append(num[i] * num[j] * num[k])
    for each in allproducts:
        if each == 0:
            allproducts.remove(each) #I think this is supposed to remove the products that are zeroes
    return max(allproducts)
num = [6,-3,-10,0,2]
print maxProductThree(num)
num = [-6,-3,-10,0,2]
print maxProductThree(num)