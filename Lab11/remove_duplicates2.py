def remove_duplicates_inplace(ls):
    ls.reverse()
    count1=0
    while count1<len(ls):  #len=8  count1=0-7
        while ls.count(ls[count1])!=1:
            ls.remove(ls[count1])
            
        count1=count1+1
    ls.reverse()
    #print(ls)
    return (ls)

raw = input()
ls = eval(raw)
print(ls)
remove_duplicates_inplace(ls)
print(ls)