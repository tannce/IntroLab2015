def distance(xa,xb,ya,yb):
    import math
    
    print('Distance between (%d, %d) and (%d, %d): '%(xa,ya,xb,yb))
    
    xx=(xb-xa)
    x=xx*xx
    yy=(yb-ya)
    y=yy*yy
    
    e=math.sqrt((x)+(y))
    print('Euclidean distance is %.2f.'%e)
    
    h=math.fabs(xb-xa)
    v=math.fabs(yb-ya)
    print('Horizontal distance is %d.'%h)
    print('Vertical distance is %d.'%v)   

    if xb==xa and yb>ya :
        dis=str('north')
    
    elif xb==xa and yb<ya :
        dis=str('south')
        
    elif xb>xa and yb==ya :
        dis=str('east')

    elif xb<xa and yb==ya :
        dis=str('west')

    elif xb>xa and yb>ya :
        dis=str('north-east')
        
    elif xb<xa and yb>ya :
        dis=str('north-west')
        
    elif xb>xa and yb<ya :
        dis=str('south-east')
        
    elif xb<xa and yb<ya :
        dis=str('south-west')
        
    elif xb==xa and yb==ya :
        dis=str('nowhere')

    print('We are going %s.'%dis)


while True:
    print('<<Point a>>')
    xa=int(input('Enter x coordinate: '))
    ya=int(input('Enter y coordinate: '))
    print('<<Point b>>')
    xb=int(input('Enter x coordinate: '))
    yb=int(input('Enter y coordinate: '))
    
    if xa==0 and ya==0 and xb==0 and xb==0 :
        print('Goodbye')
        break    
    
    else:
        distance(xa,xb,ya,yb)
    
#math.fabs(x)
#Return the absolute value of x.

#math.sqrt(x)
#Return the square root of x.