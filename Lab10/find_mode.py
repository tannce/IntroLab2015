def find_mode(l):
   #pass
   #print(l)
   
   z=len(l)
   #print(z)
   pp=[]
   keep=[]  
   count=0
   while count<=10:
      a=l.count(count)
      pp.append(a)
      
      b=l.count(count)
      keep.append(b)
      count=count+1
      
   #print(pp,'pp_count')
   #print(keep,'keep')
   
   count1=0
   while count1<10:
      if pp[0]>pp[1]:
         a=pp.pop(1)
         #print(a,'a')
      else:
         a=pp.pop(0)
         #print(a,'a')
      count1=count1+1

   #print(pp,'pp_max[]')
   ppp=pp.pop(0)
   #print(ppp,'ppp_max')
   
   for i in range(10):
      ans=keep.index(ppp)
      keep[ans]=0
      print(ans)
      if keep.count(ppp)==0:
         break

p=[]
x=1
while x<=20:
   h=int(input("Enter score: "))
   
   if h<0 or h>10:
      print('Score is out of range.')
      x=x-1
   elif h>=0 and h<=10:
      p.append(h)
      #print(p)

   x=x+1

print('-----')   
print('Original list:')
print(p)
print('Mode of scores:')
list_=find_mode(p)