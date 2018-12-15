p=[]
x=1
while x<=20:     # x=people
   
   h=int(input("Enter score: "))    # h=score
   
   if h<0 or h>10:
      print('Score is out of range.')
      
   elif h>=0 and h<=10:
      
      p.append(h)
      #print(p)
      
      p0=p.count(0)
      p1=p.count(1)
      p2=p.count(2)
      p3=p.count(3)
      p4=p.count(4)
      p5=p.count(5)
      p6=p.count(6)
      p7=p.count(7)
      p8=p.count(8)
      p9=p.count(9)
      p10=p.count(10)

      
   x=x+1
print('Original list:')
print(p)
print(' 0',p0*'*')
print(' 1',p1*'*')
print(' 2',p2*'*')
print(' 3',p3*'*')
print(' 4',p4*'*')
print(' 5',p5*'*')
print(' 6',p6*'*')
print(' 7',p7*'*')
print(' 8',p8*'*')
print(' 9',p9*'*')
print('10',p10*'*')