s=str(input())
x=int(input())


for i in s:
        if i.isalnum() or i.isdigit():
                
                ##print(i)
                ##print(ord(i))
            
                if i.islower():
                        xx=0
                        ##print(i,'low')
                elif i.isupper():
                        xx=1
                        ##print(i,'up')
                elif i.isdigit():
                        xx=2
            
                ii=ord(i)
                temp=ii+x
                ##print(temp)
                
                while temp>57 and xx==2 :   ## 0-9
                        temp-=10
                        
                while temp>90 and xx==1 :   ## A-Z
                        temp-=26
                
                while temp>122 and xx==0 :  ## a-z
                        temp-=26
                
                while temp<48 and xx==2:    ## 0-9 inv
                        temp+=10
                
                while temp<65 and xx==1:    ## A-Z inv
                        temp+=26
                    
                while temp<97 and xx==0:    ## a-z inv
                        temp+=26
                        
                print(chr(temp),end='')
                        
        else:
                print(i,end='')

# ord() --> str  
# chr() --> number
#---------
#chr(32)
#' '
#---------
#ord('0')
#48
#ord('9')
#57
#---------
#chr(97)
#'a'
#chr(122)
#'z'
#---------
#chr(65)
#'A'
#chr(90)
#'Z'