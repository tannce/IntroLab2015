s=str(input())

ss=['a','e','i','o','u','A','E','I','O','U']

for i in s:
    #print(i)
    if i in ss:
        print(i.capitalize(),end='')
        #print(i)
    else:
        print(i.lower(),end='')