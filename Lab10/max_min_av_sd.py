import math
def find_sd(l):
   z1=sum(l)
   z2=len(l)
   z=z1/z2
   
   list_=[]
   for i in l:
      list_.append((i-z)**2)
      
   sn=(((1/z2))*sum(list_))**.5
   

   print('Standard deviation is %.2f.'%sn)   

#Score range 0-100
p=[]
while True:
   h=float(input("Enter score: "))
   
   if h==-1:
      break
   elif h<0 or h>100 :
      print('Score is out of range.')
   elif h>=0 and h<=100:
      #print('pass')
      if h==-0:
         h=0
      p.append(h)
      #print(p)
   

if p!=[]:
   x=max(p)
   y=min(p)
   z1=sum(p)
   z2=len(p)
   z=z1/z2
   print('Maximum score is %.2f.'%x)
   print('Minimum score is %.2f.'%y)
   print('Average score is %.2f.'%z)
   find_sd(p)
