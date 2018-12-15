#BMI
w=float(input(''))
h=float(input(''))

bmi=w/(h*10**-2)**2
#print('%.2f' %bmi)
if bmi<18.5:
    print("1")
elif bmi >=18.5 and bmi<25:
    print('2')
elif bmi >=25 and bmi <30:
    print('3')
elif bmi >=30:
    print('4')
