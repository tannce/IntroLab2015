priceA = 6
priceB = 3
priceC = 2

qtyA = int(input('Enter quantity of A: '))
qtyB = int(input('Enter quantity of B: '))
qtyC = int(input('Enter quantity of C: '))

if qtyA<qtyB or qtyA<=0:
    print("Incorrect order - too few As.")
    if qtyB<=0:
        print("Incorrect order - too few Bs.")
    if qtyC<qtyA*2 or qtyC<=0:
        print("Incorrect order - too few Cs.")
        
elif qtyC<qtyA*2 or qtyC<=0:
    if qtyB<=0:
        print("Incorrect order - too few Bs.")
    print("Incorrect order - too few Cs.")

elif qtyB<=0:
        print("Incorrect order - too few Bs.")
else:
    print("Total amount due is %.2f baht." %(qtyA*priceA+qtyB*priceB+qtyC*priceC))