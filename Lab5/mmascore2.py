
count=1
num=0
maxScore=-1
minScore=101

numStudents =int(input("Enter number of students: "))

if numStudents<=0:
    print('Invalid number of students, program is terminated.')
else:
    while count<=numStudents :
        score = float(input('Enter score: '))
        if score>100 or score<0:
            print("Score is out of range.")        
        else:
            count=count+1
            num=num+score
            
            if score<minScore:
                minScore=score
            if score>maxScore:
                maxScore=score        
        
        
    avgScore = num/numStudents
        
    print('Maximum score is %.2f' %maxScore)
    print('Minimum score is %.2f' %minScore)
    print('Average score is %.2f' %avgScore)        