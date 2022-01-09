# call example: D:/bart/python/juldate22/cal_v0.1.py

# Program to display calendar of the given month and year

# importing calendar module
import calendar

def monthfil(yy,mm,weekday):
    mr = calendar.monthrange(yy,mm)
    si = 7 - weekday + mr[0]
    print(mr[0],si,weekday,mr[1])
    daylist = ['ma','di','wo','do','vr','za','zo']
    result = []
    ic = 0
    for i in range(weekday,7):
        result.append(daylist[i])
        ic = ic+1
    for i in range(0,weekday):
        result.append(daylist[i])
        ic = ic+1
    for i in range(si):
        result.append(' ')
        ic = ic+1
    for i in range(1,mr[1]+1):
        result.append(str(i))
        ic = ic+1
    for i in range(ic,6*7):
        result.append(' ')
        ic = ic+1
    return result

yy = 2011  # year
mm = 12    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

# deze werkt niet a1 = calendar.monthdatescalendar(yy,mm)

print(calendar.weekday(yy,mm,1)) # Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

print(calendar.monthrange(yy,mm)) # Returns weekday of first day of the month and number of days in month, for the specified year and month.

x = monthfil(yy,mm,6)
print(x)
