def decToBase(d, base):
    num1=0
    
    while d>=1:
        num=d%base                       #num/
        #print("%d"%num)
        if num1==0:
            num1=str(num)                 #print 0
            #print("%s"%num1)
        elif num1!=0:
            num1=str(num)+str(num1)          #num/
            #print("%s"%num1)
        d=d//base
        
    return num1
BASE = 2
number = int(input('Enter a decimal number (0-1000): '))

if number>1000 or number<0:
    print('Number is out of range, program is terminated.')
else:
    strBase = decToBase(number, BASE)
    print('%d in decimal is %s in binary.' %(number, strBase))
