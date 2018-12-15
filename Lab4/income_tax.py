def calNIT(income):
    if income>=1 and income<=30000:
        returnMoney=income*20/100
        return returnMoney
    
    elif income>30000 and income<=79999:
        x=income-30000
        y=income-x
        returnMoney=(y*20/100)-(x*12/100)
        return returnMoney        
    

age=int(input("Enter your age: "))
income=int(input("Enter your net ncome: "))

if age>=16 and age<=65 :
    if income>=1 and income<=80000:
        returnMoney = calNIT(income)
        print("You nagative income tax is %.2f baht." %returnMoney)
    else:
        print("Invalid income")
else:
    print("Invalid age")