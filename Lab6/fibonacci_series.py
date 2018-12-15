num=int(input('Enter a number: '))

if num<2:
    print('Invalid input, program terminates.')
else:
    count=0
    
    while count<=num:
           
        if count==0:
            x=0
            print('%d: %d' %(count,x))

        if count==1:
            y=1
            print('%d: %d' %(count,y))

        if count==2:

            temp=x+y
            print('%d: %d' %(count,temp))
        if count>2:
            x=y
            y=temp
            temp=y+x 
            print('%d: %d' %(count,temp))
            
        count=count+1


#---------------------#
#
# number 2   x=0    y=1    temp=x+y       0+1=1       ---------(z)=x+y
# x y z 
# 0 1 1
# number 3      x=y     y=temp        temp=x+y  1+1=2
# x y z
# 1 1 2
#---------------------#
# Enter a number: 8
# 0: 0
# 1: 1
# 2: 1
# 3: 2
# 4: 3
# 5: 5
# 6: 8
# 7: 13
# 8: 21
#---------------------#