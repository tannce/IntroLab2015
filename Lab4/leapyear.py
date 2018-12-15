def isLeapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return year


year=int(input("Enter year: "))

if year>=1800:
    if isLeapYear(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")    
else:
    print("Invalid year.")