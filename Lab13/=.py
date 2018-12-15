
li=[]
check=[]
while True:
    x=input()
    if x=='-1':
        break
    else:
        x=x.split('=')
        
        
        x[0]=x[0].strip()
        x[1]=x[1].strip()
        
        li.append(x)
        check.append(len(x[0]))
       
for i in range(len(li)):

    print(li[i][0].rjust(max(check),' '),'=', li[i][1])