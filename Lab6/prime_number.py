def isPrime(num):
    if num==2:
        print("%d is a prime number." %num)
        
    if num==4:
        print("%d is not a prime number." %num)
        
    if num==3:
        print("%d is a prime number." %num)    
    if num==5:
        print("%d is a prime number." %num)
    if num==7:
        print("%d is a prime number." %num)     

        
    elif num!=2 and num!=3 and num!=5 and num!=7 and num!=4:
        if num%2==0 or num%3==0 or num%5==0 or num%7==0:
            print("%d is not a prime number." %num)   
        
   
        elif num%2!=0 or num%3!=0 or num%5!=0 or num%7!=0:
            print("%d is a prime number." %num)
      
#main program
while True:
    
    num=int(input("Enter a number: "))
    
    if num==0:
        break
    elif num==1:
        print("Invalid input, try again.")
    elif num<0:
        print("Invalid input, try again.")     
    else:
 
        isPrime(num)
        
print('End of program, goodbye.')