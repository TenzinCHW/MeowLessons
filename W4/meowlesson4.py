#Problem 2
print "Problem 2\n"
def compoundVal6Months(monthlyAmt, annualRate, months):
    monthlyrate = annualRate/12.0
    total = 0
    for i in range(months):
        total = (total + monthlyAmt)*(1+monthlyrate)
    return round(total,2)

#Problem 3
print "Problem 3\n"
def findAverage(listOfLists):
    total = 0 
    eachaverage = []
    count = 0
    for i in range(len(listOfLists)):
        b = 0
        for j in listOfLists[i]:
            b = b + j
            total = total + j
            count = count + 1
        if listOfLists[i] == []:
            eachaverage.append(0.0)
        else:
            eachaverage.append(round(b/float(len(listOfLists[i])),2))
    totalaverage = total/float(count)
    return eachaverage, totalaverage

print "Test case 1: findAverage([[3,4],[5,6,7],[-1,2,8]])"
ans = findAverage([[3,4],[5,6,7],[-1,2,8]])
print ans
print "Test case 2: findAverage([[13.13,1.1,1.1],[],[1,1,0.67]])"
ans = findAverage([[13.13,1.1,1.1],[],[1,1,0.67]])
print ans
print "Test case 3: findAverage([[3.6],[1,2,3],[1,1,1]])"
ans = findAverage([[3.6],[1,2,3],[1,1,1]])
print ans

#Problem 4
print "Problem 4\n"
def transposeMatrix(a):
    ans = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if len(ans) != len(a[i]):
                ans.append([a[i][j]])
            else:
                ans[j].append(a[i][j])
    return ans

print "Test case 1: a = [[1,22,13], [7,5,6], [7,8,10]]"
ans = transposeMatrix([[1,22,13], [7,5,6], [7,8,10]])
print ans
print "Test case 2: a = [[-11,12,3], [4,-5,6]]"
ans = transposeMatrix([[-11,12,3], [4,-5,6]])
print ans
print "Test case 3: a = [[1,2], [10,5], [0,0]]"
ans = transposeMatrix([[1,2], [10,5], [0,0]])
print ans

#Problem 5
print "Problem 5\n"
def getDetails(name, key, phonebook):
    for person in phonebook:
        if name is person['name']:
            return person[key]

phonebook=[{'name':'Andrew', 'mobile_phone':9477865, 'office_phone':6612345, 'email':'andrew@sutd.edu.sg'}, {'name':'Bobby', 'mobile_phone':8123498, 'office_phone':6654321, 'email':'bobby@sutd.edu.sg'}]

print getDetails ('Andrew', 'mobile_phone', phonebook)
print getDetails ('Andrew', 'email', phonebook)
print getDetails ('Bobby', 'office_phone', phonebook)
print getDetails ('Chokey', 'office_phone', phonebook)

#Problem 6
print "Problem 6\n"
def getBaseCounts(dna):
    count = {}
    for i in dna:
        if i in 'ACTG':
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1
        else:
            return 'The input DNA string is invalid'
    return count

print "Test Case 1:'AACCGT'"
ans = getBaseCounts('AACCGT')
print "Output: ", ans
print "Test Case 2: 'A'"
ans = getBaseCounts('A')
print "Output: ", ans
print "Test case 4: 'AAB'"
ans = getBaseCounts('AAB')
print "Output: ", ans
print "Test case 5: 'Aa'"
ans = getBaseCounts('Aa')
print "Output: ", ans