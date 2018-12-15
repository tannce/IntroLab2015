x=input()

li1=[]
li2=[]

for i in range(len(x)):
    if i <len(x)//2:
        li1.append(i)
    else:
        li2.append(i)
li2.reverse()

for i in range(len(li2)):
    if li1!=[]:
        a=li1.pop(0)
        print(x[a],end='')
        
    b=li2.pop(0)
    print(x[b],end='')


# x = 1234567
# li1=[0,1,2]
# li2=[3,4,5,6]
# li2.reverse()   li2=[6,5,4,3]

# x = abcdef
# li1=[0,1,2]
# li2=[3,4,5]
# li2.reverse()   li2=[5,4,3]