x=input()
li=[]

j= ' \/*:|"<>'

count=x.count('.')

for i in x:
   if i in j :
      p = '_'
      x=x.replace(i,p)
      
x=x.replace('.','_',count-1)


if x.count('.')>=1 and len(x)>15:
   
   x=x.split('.')


   if len(x[0])>15 and len(x[1])>3:
      print(x[0][:15]+'.'+x[1][:3])
   
else:
   print(x[:15])