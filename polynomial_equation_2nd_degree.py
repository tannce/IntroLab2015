# Name: Wongpiwat Sangiam ID: 5810450415 Problem 1

def isPerfectSq(n):
    x=0
    while x<n:
        
        if x**2==n:
            return ('True')
    
        x=x+1
        
    if x**2!=n:
        return ('False')