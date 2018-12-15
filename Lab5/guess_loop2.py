def evaluateGuess(guess):
    
    if guess>100:
        print("Sorry, your guess is out of range.")
    elif guess<0:
        print("Sorry, your guess is out of range.")
        
    else:
        if guess==TARGET:
            print("Congratulations, your guess is correct.")

        elif guess<TARGET:
            print("Sorry, your guess is too low.")
        else:
            print("Sorry, your guess is too high.")
    
TARGET=72
countGuess=0

while countGuess<=100:
    guess=int(input("Enter your guess: "))
    evaluateGuess(guess)
    countGuess=countGuess+1
    if guess==72:
        break
    
    

print("Total number of guesses is %d." %countGuess)