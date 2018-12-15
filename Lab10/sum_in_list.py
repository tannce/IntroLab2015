def accum_sum(l):
     #print(l)
     x=len(l)
     #print(x)
     
     count=1
     pp=0
     while count<=x:
          p=l.pop(0)
          
          z=p+pp

          pp=z
          
          print(z)
          count=count+1

list_=[]
while True:
     n=int(input('Enter a number (0 to end): '))
    
     if n==0:
          break
     elif n<1 or n>100:
          print('Number is out of range.')
     elif n>1 or n<100:
        
          list_.append(n)

#print(list_)
print('Original list:')
print(list_)
print('Accumulative Sum:')
accum_sum(list_)
