def digit(num):
    return n%10

def tens(num):
    return (n%100)//10

def hundreds(num):
    return (n%1000)//100

def thousands(num):
    return (n%10000)/1000
def sum_digits(num):
    return digit(n)+tens(n)+hundreds(n)+thousands(n)

n=int(input("Enter a number (0 to 9999): "))
print("Digit place is %d." %(digit(n)))
print("Tens place is %d." %(tens(n)))
print("Hundreds place is %d." %(hundreds(n)))
print("Thousands place is %d." %(thousands(n)))
print("Sum of all digits is %d." %(sum_digits(n)))