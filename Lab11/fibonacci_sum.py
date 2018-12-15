num=int(input())
strx=str(input())

one=[]
two=[]

if num>=0 :
    if strx.lower()=='e' or strx.lower()=='o':
        num=num+1
        for i in range(num):
            if i==0:
                x=1
                #print(x)
                if i%2!=0:
                    one.append(x)
                else:
                    two.append(x)
            if i==1:
                y=1

                #print(y)
                if i%2!=0:
                    one.append(y)
                else:
                    two.append(y)                
            if i>=2:
                temp=x+y
                x=y
                y=temp

                #print(temp)
                if i%2!=0:
                    one.append(temp)
                else:
                    two.append(temp)                
    else:
        print('ERROR')    
else:
    print('ERROR')
 
if strx.lower()=='o' and sum(one)==0:
    print('ERROR')
    
elif strx.lower()=='e' and num>=0:
    print(sum(two))
          
elif strx.lower()=='o' and num>=0:
    print(sum(one))