num=int(input('Enter a number: '))

if num<=0:
    print('Invalid input, program terminates.')
else:
    
    count=1
    while count<=num:
        print("*"*count)
        #print()
        count=count+1
    

    #print ("%d"%count)
    #print ("%d"%num)
    
    count=count-2
    while count>=1:
        #print("test")
        
        print("*"*count)
        count=count-1