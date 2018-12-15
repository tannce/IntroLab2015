x=str(input())

l=len(x)
ll=l-3
ll2=l-4

ans1='T'

no=',.1234567890'
no1=','
no2='.'
count=x.count('.')

com=0
dot=0

for i in x:          ## check digit
    if i in no:
        if i in no1: ## have comma
            com=1
            
        if i in no2: ## have dot
            dot=1
            
        if count>1:  ## count dot
            ans1='F'
    else:
        ans1='F'

if com==1:           ## check comma
    if dot==0:
        s = x.split(",")
        le=len(s[1])
        if le != 3 :
            ans1='F'      
        else:
            ans1='T'
    else:
        kuy=x.split('.')
        kkuy=kuy[0]
        s=kkuy.split(",")
        le=len(s[1])
        if le != 3 :
            ans1='F'
        else:
            kk=kkuy.find(",")
            y = kkuy[0:kk]
            l = len(y)
            if l > 3 :
                ans1='F'
            else:            
                ans1='T'
        
if ans1=="T":                     ## Answer
    if com==0 and dot==0:         ## NO!! comma and dot 
        x=int(x)
        print(x+1)     
    
    elif x[ll]=='.' and dot==1:   ## check dot
        if com==1:                ## have dot and comma
            x=x.replace(',','')
            x=x.split('.')
            x[0]=int(x[0])
            x[0]=x[0]+1
            x[0]=str(x[0])
            print(x[0]+'.'+x[1])            
            
        else:
            x=x.split('.')
            x[0]=int(x[0])
            x[0]=x[0]+1
            x[0]=str(x[0])
            print(x[0]+'.'+x[1])
        
    elif x[ll2]==',' and com==1:   ## check comma
        x=x.replace(',','')
        x=int(x)
        x=x+1
        print(x)        
        
    else:
        ans1='F'
        
if ans1=='F':
    print('ERROR')