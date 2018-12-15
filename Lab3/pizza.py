import math

def get_size():
    d=str(input("Select pizza size (s-small, m-medium, l-large): "))
    return d
    
def get_price(diameter):
    p=str(input("More pepperoni (y/n)?: "))
    c=str(input("More cheese (y/n)?: "))
    m=str(input("More mushroom (y/n)?: "))
    
    if d=="s" or d=="S":
        diameter=10
        
    elif d=="m" or d=="M":
        diameter=12
        
    elif d=="l" or d=="L":
        diameter=16
        
    extracost=0
    if p=="y" or p=="Y":
        extracost=0.50+extracost
    elif c=="y" or c=="Y":
        extracost=0.25+extracost    
    elif m=="y" or m=="Y":
        extracost=0.01+extracost
    
    area = math.pi*(diameter/2)**2
    cost = fixedcost+(basecost*area)+(extracost*area)
    price = 1.5*cost
    return price

fixedcost = 3.5
basecost = 2

d=get_size()
if d!="s" and d!="m" and d!="l" and d!="S" and d!="M" and d!="L" :
    print('Invalid size, try again later, bye.')
else:
    price = get_price(d)
    print('>> Price of the pizza is %.2f baht.' % price)