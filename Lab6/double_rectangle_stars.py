h=int(input('Enter height: '))
w=int(input('Enter width: '))

if h<=0:
    print('Invalid input, program terminates.')
elif w<=0:
    print('Invalid input, program terminates.')
else:
    
    count=1
    while count<=h:
        if count%2!=0:
            print("* "*w)
            #print()
            count=count+1
        else:
            print(" *"*w)
            #print()
            count=count+1  