day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))

def isLeapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return year

if isLeapYear(year):
    x=1
    #print(year, "is a leap year.")
else:
    x=2
    #print(year, "is not a leap year.")  

def mnum(month,x):
    if month==1:
        return 31
    if month==2:
        if x==1:
            return 29
        else:
            return 28
    if month==3:
        return 31
    if month==4:
        return 30
    if month==5:
        return 31
    if month==6:
        return 30
    if month==7:
        return 31   
    if month==8:
        return 31
    if month==9:
        return 30
    if month==10:
        return 31
    if month==11:
        return 30
    if month==12:
        return 31


def mname(month):
    if month==1:
        return "January"
    if month==2:
        return "February"
    if month==3:
        return "March"
    if month==4:
        return "April"
    if month==5:
        return "May"    
    if month==6:
        return "June"    
    if month==7:
        return "July"    
    if month==8:
        return "August"
    if month==9:
        return "September"
    if month==10:
        return "October"
    if month==11:
        return "November"
    if month==12:
        return "December"


def alldays(numdays,x):
    if x==1:
        y=366-numdays
        return y
    else:
        y=365-numdays
        return y

def dnum(day,month,x):
    if month==1:   #jan
        num=day
        return num
    if month==2:   #feb
        num=day+31
        return num
    if month==3:   #mar
        if x==1:
            num=day+60
            return num
        else:
            num=day+59
            return num
    if month==4:    #apr
        if x==1:
            num=day+91
            return num
        else:
            num=day+90
            return num
    if month==5:    #may
        if x==1:
            num=day+121
            return num
        else:
            num=day+120
            return num
    if month==6:    #jun
        if x==1:
            num=day+152
            return num
        else:
            num=day+151
            return num
    if month==7:    #july
        if x==1:
            num=day+182
            return num
        else:
            num=day+181
            return num
    if month==8:    #aug
        if x==1:
            num=day+213
            return num
        else:
            num=day+212
            return num
    if month==9:    #sep
        if x==1:
            num=day+244
            return num
        else:
            num=day+243
            return num
    if month==10:   #oct
        if x==1:
            num=day+274
            return num
        else:
            num=day+273
            return num
    if month==11:   #nov
        if x==1:
            num=day+305
            return num
        else:
            num=day+304
            return num
    if month==12:   #dec
        if x==1:
            num=day+335
            return num
        else:
            num=day+334
            return num
    else:
        num=day+0
        return num

numbermonth=mnum(month,x)
numdays=dnum(day,month,x)
monthname=mname(month)
#print("%s"%monthname)
numbledays=alldays(numdays,x)
#print("%d"%numbledays)

if x==1: #leap year
    if year<=0:
        print('Invalid year.')
        
    elif month>12 or month<1:
        print("Invalid month.")
        
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day>31 or day<1:
            print("Invalid day.")

        else:
            print("%d %s %d is day number %d." %(day,monthname,year,numdays))
            print("There are %d days remaining in this year." %(numbledays))    
            
    elif month==2:
        if day>29 or day<1:
            print("Invalid day.")
    
        else:
            print("%d %s %d is day number %d." %(day,monthname,year,numdays))
            print("There are %d days remaining in this year." %(numbledays))  
            
    elif month==4 or month==6 or month==9 or month==11:
        if day>30 or day<1:
            print("Invalid day.")   

        else:
            print("%d %s %d is day number %d." %(day,monthname,year,numdays))
            print("There are %d days remaining in this year." %(numbledays))
    
if x==2: #isn't leap year
    if year<=0:
        print('Invalid year.')
        
    elif month>12 or month<1:
        print("Invalid month.")
        
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day>31 or day<1:
            print("Invalid day.")

        else:
            print("%d %s %d is day number %d." %(day,monthname,year,numdays))
            print("There are %d days remaining in this year." %(numbledays))        
    elif month==2:
        if day>28 or day<1:
            print("Invalid day.")

        else:
            print("%d %s %d is day number %d." %(day,monthname,year,numdays))
            print("There are %d days remaining in this year." %(numbledays))        

    elif month==4 or month==6 or month==9 or month==11:
        if day>30 or day<1:
            print("Invalid day.")   

        else:
            print("%d %s %d is day number %d." %(day,monthname,year,numdays))
            print("There are %d days remaining in this year." %(numbledays))