


def printMainMenu():
    print('---<< Main Menu >>---')
    print('    <B>urger Meal')
    print('    <C>hicken Meal')
    print('    <P>asta Meal')
    m=str(input("Enter your choice: "))
    return m.lower()


def doSubMenu(mchoice):
    if mchoice=="b":
        return burgerSub()
    elif mchoice=="c":
        return chickenSub()
    elif mchoice=="p":
        return pastaSub()
    else:
        return "0"


def burgerSub():
    print('---<< Burger Sub Menu >>---')
    print('    <R>egular Burger')
    print('    <C>heese Burger')
    print('    <D>ouble Cheese Burger')
    schoice = input('Enter your choice: ')
    a=schoice.lower()
    
    
    if a=="r":
        price=60
        x=("Your Regular Burger is %d Baht." %price)
        return x
    elif a=="c":
        price=75
        x=("Your Cheese Burger is %d Baht." %price)
        return x
    elif a=="d":
        price=90
        x=("Your Double Cheese Burger is %d Baht." %price)
        return x
    else:
        return "-1"
    
    
    
def chickenSub():
    print('---<< Chicken Sub Menu >>---')
    print('    <F>ried Chicken')
    print('    <G>rilled Chicken')
    print('    <C>hef\'s Chicken')
    schoice = input('Enter your choice: ')
    a=schoice.lower()
    
    if a=="f":
        price=120
        x=("Your Fried Chicken is %d Baht." %price)
        return x
    elif a=="g":
        price=150
        x=("Your Grilled Chicken is %d Baht." %price)
        return x
    elif a=="c":
        price=180
        x=("Your Chef\'s Chicken is %d Baht." %price)
        return x
    else:
        return "-1"
    
    
    
def pastaSub():
    print('---<< Pasta Sub Menu >>---')
    print('    <S>paghetti de Italiano')
    print('    <L>asagna Supreme')
    print('    <M>acaroni Special')
    schoice = input('Enter your choice: ')
    a=schoice.lower()
    
    if a=="s":
        price=90
        x=("Your Spaghetti de Italiano is %d Baht." %price)
        return x
    elif a=="l":
        price=120
        x=("Your Lasagna Supreme is %d Baht." %price)
        return 
    elif a=="m":
        price=100
        x=("Your Macaroni Special is %d Baht." %price)
        return x
    else:
        return "-1"
mchoice = printMainMenu()
   
message = doSubMenu(mchoice)
    
if message == '0':
    print('Invalid main menu choice.')
elif message == '-1':
    print('Invalid sub menu choice.')
else:
    print(message)