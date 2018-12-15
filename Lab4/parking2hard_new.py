hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))
import math


if hours<0 or hours>20 or minutes<0 or minutes>59 or buyAmt<0 or (hours==20 and minutes>0):
   print("Invalid time.")
elif buyAmt<300:
   if hours<=1:
      print("No charge, thank you.")
   elif hours==2 and minutes==0:
      print("No charge, thank you.")
   elif hours<=3 and minutes>=1:
      q=20*(hours-2)+math.ceil(minutes/60)*20
      print("Total amount due is %d Baht, thank you." %q)
   elif hours>=4:
      q=(hours-4)*50+50*math.ceil(minutes/60)+40
      print("Total amount due is %d Baht, thank you." %q)
elif buyAmt>=300 and buyAmt<=3000:
   if hours<=3:
      print("No charge, thank you.")
   elif hours>=4:
      q=(hours-4)*50+50*math.ceil(minutes/60)
      print("Total amount due is %d Baht, thank you." %q)
elif buyAmt>3000:
   print("No charge, thank you.")
