x=input()
li=[]
a=x.split(',')
for i in a:   #a=['a', 'b', 'c', 'd', 'e']
    #print(i)
    i=i.strip()
    st='"'
    ans=st+i+st
    li.append(ans)
    
print(",".join(li))

    #print(ans,end='')
    #print(ans)