#Homework 4
#Problem 1
print "Problem 1\n"
def getConversionTable():
	F = []
	C =[]
	CApprox = []
	for Ftemp in range(0,101,10):
		F.append(Ftemp)
		C.append(round((Ftemp - 32)/9.0*5, 1))
		CApprox.append((Ftemp - 30)/2.0)
	conversion = [F,C,CApprox]
	return conversion
print getConversionTable()

#Problem 2
print "Problem 2\n"
def maxList(inp):
	thelist = []
	for alist in inp:
		thelist.append(max(alist))
	return thelist

#Problem 3
print "Problem 3"
def nBynMultiplicationTable(N):
	table = []
	if N < 2:
		return None
	else:
		count = 1
		while count <= N:
			smalltable = []
			for o in range(1,N+1):
				smalltable.append(count*o)
			table.append(smalltable)
			count = count + 1
		return table

#Problem 4
print "Problem 4\n"
def mostFrequent(numList):
	damfrequent = []
	allnum = {}
	for num in numList:
		if num in allnum:
			allnum[num] = allnum[num] + 1
		else:
			allnum[num] = 1
	maxfrequency = max(allnum.values())
	for numbers in allnum:
		if allnum[numbers] == maxfrequency:
			damfrequent.append(numbers)
	return damfrequent

a = [1,23,4,5,6,4,6,8]
print mostFrequent(a)

#Problem 5
print "Problem 5\n"
def diff(p):
	dp = {}
	for x in p:
		if x > 0:
			dp[x-1] = x*p[x]
	return dp