#Problem 1a
# x
# y
# x+y
#1b
# x+y
# y
# idk
# x

#Problem 2
def letterGrade(mark):
    if mark >= 90 and mark <= 100:
        return 'A'
    elif mark >= 80 and mark < 90:
        return 'B'
    elif mark >= 70 and mark < 80:
        return 'C'
    elif mark >= 60 and mark < 70:
        return 'D'
    elif mark >=0 and mark <60:
        return 'E'


print letterGrade(102)
print letterGrade(100)
print letterGrade(83)
print letterGrade(75)
print letterGrade(67)
print letterGrade(52)
print letterGrade(-2)

#Problem 3
def check1(n1, n2):
    return n1 > n2

print check1(2, -1)
print check1(-1, 2)
print check1(2, 2)

#Problem 4
def listSum(a):
    total = 0
    for i in a:
        total += i
    return round(total, 1)

print "Test case 1: [4.25 ,5.0 ,10.75]"
ans = listSum([4.25 ,5.0 ,10.75])
print ans
print "Test case 2: [5.0]"
ans = listSum([5.0])
print ans
print "Test case 3: []"
ans = listSum([])
print ans

#Problem 5
def maxList(a):
    if a == []:
        return (None, None)
    else:
        x = a[0]
        y = a[0]
        for i in range(len(a)):
            if a[i] > y:
                y = a[i]
            if a[i] < x:
                x = a[i]
    return (x, y)

print "Test case 1: [1,2,3,4,5]"
ans = maxList([1,2,3,4,5])
print ans
print "Test case 2: [1,1,3,0]"
ans = maxList([1,1,3,0])

print ans
print "Test case 3: [3,2,1]"
ans = maxList([3,2,1])
print ans
print "Test case 4: [0,10]"
ans = maxList([0,10])
print ans
print "Test case 5: [1]"
ans = maxList([1])
print ans
print "Test case 6: []"
ans = maxList([])
print ans

#Problem 6
def isPalindrome(a):
    return str(a) == str(a)[::-1]

print "Test case 1: 1"
ans = isPalindrome(1)
print ans
print "Test case 2: 22"
ans = isPalindrome(22)
print ans
print "Test case 3: 12321"
ans = isPalindrome(12321)
print ans
print "Test case 4: 441232144"
ans = isPalindrome(441232144)
print ans
print "Test case 5: 4412321144"
ans = isPalindrome(4412321144)
print ans
print "Test case 6: 144"
ans = isPalindrome(144)
print ans