def check_order(l):
   p1.append(l)
   #print(p1)
   return p1    

def copylist1(l):
   p2.append(l)
   return p2

def copylist2(l):
   p3.append(l)
   return p3

p1=[]
p2=[]
p3=[]
while True:
   x=int(input("Enter a number (-1 to end): "))
   if x==-1:
      break
   elif x<0 or x>100:
      print('Number is out of range.')
   elif x>0 or x<100:
      #check_order(x)
      l1=check_order(x)
      l2=copylist1(x)
      l3=copylist2(x)

if p1==[]:
   l1=[]
   l2=[]
   l3=[]
   
print('-----')
print('Original list:')
print(l1)

l2.sort()
l3.sort(reverse=True)

z=len(l1)
zz=z-2

if len(l1)==3:
   zz=z-1

sumx=0
if l1==[] and l2==[]:
   print('The list is empty.')

elif l1==l2:
   for i in range(zz):
      if l1[0]==l1[1]:
         l1.pop(0)
         sumx=1
      else:
         sumx=2
         
   if sumx==1:
      print('The list is in non-increasing and non-decreasing order.')
      
   elif sumx==0:
      if l1[0]==l2[0]:
         print('The list is in non-increasing and non-decreasing order.')       
   else:
      print('The list is in non-decreasing order.')
      
elif l1==l3:
   print('The list is in non-increasing order.')

else:
   print('The list is in random order.')