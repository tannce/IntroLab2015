#RGB Color

r=int(input('Enter Red Value: '))
g=int(input('Enter Green Value: '))
b=int(input('Enter Blue Value: '))

# Color range(0-255)

if r<0 or r>255:
    print('Invalid value.')
elif g<0 or g>255:
    print('Invalid value.')
elif b<0 or b>255:
    print('Invalid value.')
else:
    if r>=0:
        numr='{0:08b}'.format(r)  #dec to bin
        #print('%s'%numr)

    if g>=0:
        numg='{0:08b}'.format(g)
        #print('%s'%numg)

    if b>=0:
        numb='{0:08b}'.format(b)
        #print('%s'%numb)

    num=str(numr)+str(numg)+str(numb)
    print('%s'%num)
        
    x=int('%s'%num,2)
    print('Color value is %s.' %x)