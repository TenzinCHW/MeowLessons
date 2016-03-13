import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code
import math

#Problem 1
print "Problem 1\n"
def rolldice():
    return random.randint(1,6)

def playCraps():
    luck1 = rolldice()
    luck2 = rolldice()
    total1 = luck1 + luck2
    print "You rolled %i + %i = %i"% (luck1,luck2,total1)
    if total1 == 2 or total1 == 3 or total1 == 12:
        return "You lose"
    elif total1 == 7 or total1 == 11:
        return "You win"
    else:
        print "point is %i"% total1
        luck3 = rolldice()
        luck4 = rolldice()
        total2 = luck3 + luck4
        print "You rolled %i + %i = %i"% (luck3,luck4,total2)
        if total2 == 7:
            return "You lose"
        elif total2 == total1:
            return "You win"
        while total2 != total1:
            luck3 = rolldice()
            luck4 = rolldice()
            total2 = luck3 + luck4
            print "You rolled %i + %i = %i"% (luck3,luck4,total2)
            if total2 == total1:
                return "You win"
            elif total2 == 7:
                return "You lose"

#Problem 2
print "Problem 2\n"
def leapYear(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def RRR(y,x):
    return y%x

def dayOfWeekJan1(year):
    d = RRR(1 + 5*RRR(year-1,4) + 4*RRR(year-1,100) + 6*RRR(year-1,400),7)
    return d

def numDaysInMonth(month_num,leap_year):
    if month_num in (1,3,5,7,8,10,12):
        return 31
    elif month_num in (4,6,9,11):
        return 30
    elif month_num == 2 and leap_year:
        return 29
    else:
        return 28

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    monthdict = {}
    for month in range(1,13):
        monthdict[month] = months[month-1]
    CalMonth = [monthdict.values()[month_num-1],'','','','','','']
    currentday = 0
    while currentday < num_days_in_month + 1:
        for week in range(len(CalMonth)):
            if week == 0:
                pass
            elif week == 1:
                CalMonth[week] += first_day_of_month*'  '
                for days in range(1, 7 - first_day_of_month):
                        CalMonth[week] += ' %i'% days
                        currentday += 1
            else:
                for days in range(currentday + 1, currentday + 8):
                    if currentday <= num_days_in_month:
                        CalMonth[week] += ' %i'% currentday
                        currentday += 1
    for week in CalMonth:
        if week == '':
            CalMonth.remove(week)
    return CalMonth


def constructCalYear(year):
    


# def displayCalendar(calendar_year):

