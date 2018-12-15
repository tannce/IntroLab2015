#factorial table

num=int(input("Enter a number: "))
if num<0:
        print('Invalid input, program terminates.')
else:
        count=0
        while count<=num:
                if count==0:
                        print('%d! = 1 = 1'%(count))
                        
                if count==1:
                        print('%d! = 1 = 1'%(count),end='')
                        
                if count>=2:
                        print()
                        print('%d! = '%(count ),end='')
                        
                        x=count
                        fac=1
                        
                        while x>=1:
                                #fac
                                fac=fac*x
                                
                                y=str(x)
                                
                                if y!="1":
                                        print('%s x '%y,end='')

                                else:
                                        print('%s ='%y,end='')
                                        print(' %d'%fac,end='')

                                x=x-1                        

                count=count+1