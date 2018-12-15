NUM_STUDENTS=10
count=1
num=0
maxScore=-1
minScore=101

while count<=NUM_STUDENTS:
    score=float(input("Enter score: "))
    if score>100 or score<0:
        print("Score is out of range.")
    else:
        count=count+1
        sum=sum+score
        if score<minScore:
            minScore=score
        if score>maxScore:
            maxScore=score
             
avgScore=sum/NUM_STUDENTS

print("Maximum score is %.2f" %maxScore)
print("Minimum score is %.2f" %minScore)
print("Average score is %.2f" %avgScore)