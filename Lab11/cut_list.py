ls = ['a','b','c','d','e','f','g','h','i','j', 'k', 'l']

##1. e-j
z=ls[4:10]
print(z)

##2. b-k and 3 step
z=ls[1:11:3]
print(z)

##3. first-g
z=ls[0:-5]
print(z)

##4. c-last
z=ls[2:12]
print(z)

##5. j-d and 2 backstep 
z=ls[-3:2:-2]
print(z)

##6. first-last and 3 step
z=ls[::3]
print(z)

##7. index 2 - index 9 and 2 step
z=ls[2:9:2]
print(z)

##8. rip ['g', 'e', 'c', 'a'] 
z=ls[6::-2]
print(z)