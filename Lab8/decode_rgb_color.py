num=int(input(''))

if num>16777215 or num<0:
    print('ERROR')
else:
    
    r=num>>16
    #print(r)
    rr=r&255
    print(rr)
    
    
    g=num>>8
    #print(g)
    gg=g&255
    print(gg)
    
    
    b=num>>0
    #print(b)
    bb=b&255
    print(bb)