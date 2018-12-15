# Name: Wongpiwat Sangiam ID: 5810450415 Problem 3

num=int(input(''))

nump=str(num)

#print(nump)

count=1
count1=3
count2=5
count3=7
count4=9
numx=nump.count('%d'%(count))
numx1=nump.count('%d'%(count1))
numx2=nump.count('%d'%(count2))
numx3=nump.count('%d'%(count3))
numx4=nump.count('%d'%(count4))

#print(numx1)
#print(numx2)
#print(numx3)

total=(numx1*3)+(numx2*5)+(numx3*7)+(numx*1)+(numx4*9)
if total==0:
        print('-1')
else:
        print(total)