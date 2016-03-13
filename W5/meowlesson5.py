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

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    CalMonth = [months[month_num-1],'','','','','','']
    currentday = 1
    while currentday <= num_days_in_month:
        for week in range(len(CalMonth)):
            if week == 0:
                pass
            elif week == 1:
                if first_day_of_month == 0:
                    CalMonth[week] += ' 1'
                    currentday += 1
                else:
                    CalMonth[week] += (first_day_of_month)*'   ' + ' 1'
                    currentday += 1
                for day in range(2,8-first_day_of_month):
                    CalMonth[week] += ' %2d' % day
                    currentday += 1
            else:
                for day in range(currentday,currentday+7):
                    if day <= num_days_in_month:
                        if (day+first_day_of_month-1)%7 == 0:
                            CalMonth[week] += '%2d'%day
                            currentday += 1
                        else:
                            CalMonth[week] += ' %2d'%day
                            currentday += 1
    for week in CalMonth:
            if week == '':
                CalMonth.remove(week)
    return CalMonth
            # elif week == 1:
            #     if first_day_of_month != 0:
            #         CalMonth[week] += ' ' + (first_day_of_month)*'   '
            #     else:
            #         CalMonth[week] += ' '
            #     for days in range(1, 8 - first_day_of_month):
            #         if days == 1:
            #             CalMonth[week] += '%i'% days
            #             currentday += 1
            #         else:
            #             CalMonth[week] += '  %i' % days
            #             currentday += 1
            # else:
            #     for days in range(currentday + 1, currentday + 8):
            #         if currentday < num_days_in_month:
            #             if days < 10:
            #                 if (first_day_of_month+currentday)%7 == 0:
            #                     CalMonth[week] += ' %i'% days
            #                     currentday += 1
            #                 else:
            #                     CalMonth[week] += '  %i'% days
            #                     currentday += 1
            #             else:
            #                 if (first_day_of_month+currentday)%7 == 0:
            #                     CalMonth[week] += '%i'% days
            #                     currentday += 1
            #                 else:
            #                     CalMonth[week] += ' %i'% days
            #                     currentday += 1
print constructCalMonth(1,3,31)

def constructCalYear(year):
    CalYear = [year]
    isleap = leapYear(year)
    currentday = 0
    for month in range(1,13):
        numdays = numDaysInMonth(month, isleap)
        themonth = constructCalMonth(month, (dayOfWeekJan1(year)+currentday)%7, numdays)
        CalYear.append(themonth)
        currentday += numdays
    return CalYear

def displayCalendar(calendar_year):
    CalYear = constructCalYear(calendar_year)
    printedCalYear = ''
    for item in range(1,len(CalYear)):
        for theitem in CalYear[item]:
            if theitem in months:
                if theitem != 'January':
                    printedCalYear += '\n\n'
                printedCalYear += theitem
                printedCalYear += '\n' + ' S  M  T  W  T  F  S'
            else:
                printedCalYear += '\n' + theitem
    return printedCalYear

print displayCalendar(2015)

# Problem 3
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)