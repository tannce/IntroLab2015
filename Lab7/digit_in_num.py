def count_digit(n,x):
    global strn
    
    county=10
    countx=1    
    xxx=1
    count=0

        
    while xxx<=strn:
        temp=n%county//countx
        #print(temp)
        
        county=county*10
        countx=countx*10
        
        if temp==x:
            if temp==0:
                count=count+1
            elif temp==1:
                count=count+1
            elif temp==2:
                count=count+1
            elif temp==3:
                count=count+1 
            elif temp==4:     
                count=count+1   
            elif temp==5:
                count=count+1    
            elif temp==6:
                count=count+1               
            elif temp==7:
                count=count+1               
            elif temp==8:
                count=count+1               
            elif temp==9:
                count=count+1    
            xxx=xxx+1
    #print(count)
    return count


n=int(input('Enter a number: '))
x=int(input('Enter a digit: '))

if n<0:
    print('Invalid number.')
if x<0 or x>9:
    print('Invalid digit.')
elif n>=0 and x>=0 and x<=9:
    p=str(n)
    strn=p.count('%s' %x)
    digit=count_digit(n,x)
    if digit==1:
        
        print('Digit %d occurs %d time.'%(x,digit))
    else:
        print('Digit %d occurs %d times.'%(x,digit))