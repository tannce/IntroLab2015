def remove_duplicates(t):
    #print(t) ## give list t
    
    tt=[]
    for i in t:
        #print(i)
        if tt.count(i)>0:
            #print('T')
            continue
        else:
            #print('F')
            tt.append(i)
    return tt