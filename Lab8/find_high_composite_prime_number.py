def list(a,b,c,d):
    if a>b and a>c and a>d:
        show=a
        print('%d'%show)
    elif b>a and b>c and b>d:
        show=b
        print('%d'%show)        
    elif c>a and c>b and c>d:
        show=c
        print('%d'%show)        
    elif d>a and d>b and d>c:
        show=d
        print('%d'%show)
        
        
num=int(input(''))

if num <=0:
    print('ERROR')
elif num==1:
    pass
else:
    a=0
    b=0
    c=0
    d=0
    while num>1:
        
        if num%2==0:
            num=num//2
            a=2
            
        elif num%3==0:
            num=num//3
            b=3
            
        elif num%5==0:
            num=num//5
            #print('5')
            c=5
            
        elif num%7==0:
            num=num//7
            #print('7')
            d=7
        
            

        elif num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
            a=0
            b=0
            c=0
            d=0
            print('%d'%num)
            break

    list(a,b,c,d)
                