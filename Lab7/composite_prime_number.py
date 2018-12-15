num=int(input('Enter positive integer: '))

if num<=0:
    print('Invalid number.')
elif num==1:
    pass
else:
    count=1
    
    while num>1:
        
        if num%2==0:
            num=num//2
            print('2')
            
        elif num%3==0:
            num=num//3
            print('3')
              
        elif num%5==0:
            num=num//5
            print('5')
       
        elif num%7==0:
            num=num//7
            print('7')
        elif num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
            print('%d'%num)
            break