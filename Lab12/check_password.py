ls=[]
s=str(input())
ans=0

for i in s:
    #print(i)
    ls.append(i)
#print(ls)

if len(ls)>=8:
    for i in s:
        if i.isdigit()==True:
            
            for i in s:
                if i.isupper()==True:
                    
                    for i in s:
                        if i.isalnum()==False:
                            
                            for i in s:
                                if i.isspace()==False:
                                    #print('OK')
                                    ans=1
if ans==0:
    print('WRONG')
else:
    print('OK')