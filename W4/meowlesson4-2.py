

def printvals(n):
	alist = range(1,n+1)
	for i in range(1,n+1):
		if i%3 == 0 and i%7 == 0:
			alist[i-1] = 'AB'
		elif i%3 == 0:
			alist[i-1] = 'A'
		elif i%7 == 0:
			alist[i-1] = 'B'
	return alist
print printvals(0)

#Problem 2
print "Problem 2\n"
def interlock(word1, word2, word3):
	if len(word1) != len(word2):
		return False #The first two words must be of same length
	elif len(word1) + len(word2) != len(word3): #Check if the sum of lengths of first two words are equal to length of third word. If not, they can't be interlocked to get the third word.
		return False
	else:
		theword = '' #Initialize the interlocked word
		count = 0 #Initialize a counter
		while count < len(word1): #Do the following until end of first word
			theword += word1[count] + word2[count] #Append the count-th indexed letter to interlocked word
			count += 1 #Go to next letter in word1
		return theword == word3 #Check if interlocked word is the same as the third word.

#Problem 3
print "Problem 3"
def throwNdice(n, nExp):
	chance = 5/6.0
	totalchance = 1 - chance**n
	thechance = 1 - (1 - totalchance)**nExp
	return thechance