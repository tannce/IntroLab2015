import math
def calculate_parking_fee(h, m):
    if h==0 and m<=15:
        print("No charge, thanks.")
    elif h==2:
        m=m/60
        price=(math.ceil(m)+h-1)*10
        print("Total amount due is %d Baht." %price)
    elif h<=2:
        price=10
        print("Total amount due is %d Baht." %price)
    else:
        m=m/60
        price=((h-1)+math.ceil(m))*10
        print("Total amount due is %d Baht." %price)
        
h = int(input('Enter number of hours: '))
m = int(input('Enter number of minutes: '))
        
if h<0 or m<0 or m>59:
    print("Input Error!")
else:
    calculate_parking_fee(h, m)