
n=int(input())
x=int(input())

if n>7 or x>31 or n<1 or x<1 :
   print("ERROR")
elif (x-n)%7==0:
   print("Sunday")
elif (x-n)%7==1:
   print("Monday")
elif (x-n)%7==2:
   print("Tuesday")   
elif (x-n)%7==3:
   print("Wednesday")      
elif (x-n)%7==4:
   print("Thursday")         
elif (x-n)%7==5:
   print("Friday")            
elif (x-n)%7==6:
   print("Saturday")