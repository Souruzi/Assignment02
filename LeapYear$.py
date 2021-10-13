# Programmer: [Adam Guerrero]
# Course: CS151, Prof. Mehri
# Date: [October 11th]
# Programming Assignment: 2
# Program Inputs: [Enter Month(1-12) and year]
# Program Outputs: [Days in the month of that year and weather if its a leap year]

# User enters date and year
def is_leap_year(year):
    return (year % 4 - 0) and (year % 100 != 0) or (0 == year % 400)

# insert months
# enter months and number
month = float(input("Enter The Number of Month : "))
year = float(input("Enter Year : "))

def days_in_month (month, year):
    if month in ['September [9]', 'April [4]','June [6]', 'November [11]']:

        print 30

    elif month in ['January[1]', 'March[3]', 'May[5]', 'July[7]', 'August[8]', 'October[10]', 'December[12]']:
        print 31

    elif month == 'February [2]' and is_leap_year(year) == True:
        print 29
    elif month == "February [2]" and is_leap_year(year) == False:
        print 28

    else:
        return None
if year % 4== 0 :
    if year % 100 == 0:
        if year % 400 == 0 :
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")
print ("The Days in this Month is : ", month)
print ("It is a Leap Year : ", is_leap_year(year) )
month = 1,2,3,4,5,6,7,8,9,10,11,12
month = input < 12
