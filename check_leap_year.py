def isYearLeap(year):
#
# your code from LAB 4.1.3.6
#
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

month_lengths = [31,28,31,30,31,30,31,31,30,31,30,31]

def daysInMonth(year, month):
#
# your code from LAB 4.1.3.7
#
    if isYearLeap(year):
        if month == 2:
            return month_lengths[month-1] + 1
        else:
            return month_lengths[month-1]
    else:
        return month_lengths[month-1]

def dayOfYear(year, month, day):
#
# put your new code here
#
    if year >= 1582 and (1 <= month <= 12 ) and day <= daysInMonth(year, month):
            for i in range(1,month):
                day += daysInMonth(year, i)
            return day
    else:
        return None
    
print(dayOfYear(2000, 12, 31))
