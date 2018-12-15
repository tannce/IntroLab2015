amount_buy = float(input("Enter buying amount: "))
if amount_buy>=1000 and amount_buy<3000:
    amount_due=amount_buy-(amount_buy*10/100)
    

elif amount_buy>=3000:
    amount_due=amount_buy-(amount_buy*15/100)

else:
    amount_due=amount_buy
               

print("Amount due after discount is %.2f baht." %amount_due)
