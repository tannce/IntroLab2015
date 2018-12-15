n=input()

li1={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

li2={'11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19': 'nineteen'}

li3={'10':'ten','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}

li4={'1':'ten','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}

if len(n)<=3 and n.isdigit():
    if len(n)==3:                             ## len==3
        
        if n[0] in li1:                       ## 1-9 hundred
            if n[1:] in li2:                  ## 11-19 ten
                print(li1[n[0]]+'-hundred-'+li2[n[1:]])
                
            elif n[1:] in li3:                ## 10-90 ty
                print(li1[n[0]]+'-hundred-'+li3[n[1:]])
                
            elif n[1:2] in li4:               ## ten-unit ex 155
                if n[2] in li1:
                    print(li1[n[0]]+'-hundred-'+li4[n[1:2]]+'-'+li1[n[2]])
                
            elif n[1:]=='00':                 ## 00
                print(li1[n[0]]+'-hundred')
                
            elif n[2] in li1:                 ## 1-9 unit
                print(li1[n[0]]+'-hundred-'+li1[n[2]])
                
        else:                                 ## 0 hundred
            if n[1:] in li2:                  ## 0 11-19 ex 011
                print(li2[n[1:]])
                
            elif n[1:] in li3:                ## 0 ty ex 090
                print(li3[n[1:]])
            
            elif n[1] in li1:                 ##  ten-unit ex 55
                if n[2] in li1:
                    print(li4[n[1]]+'-'+li1[n[2]])
            
            elif n[2] in li1:                 ## 0 unit ex 5
                print(li1[n[2]])
                
            elif n[2]=='0':                   ## zero ex 000
                print('zero')
    else:
        if len(n)==2:                  ## len==2
            if n in li3:               ## 10-90 ten
                print(li3[n])
                
            elif n=='00':
                print('zero')
                
            elif n in li2:             ## 11-19 ten
                print(li2[n])
                
            elif n[0] in li4:          ## ten unit ex 22
                if n[1] in li1:
                    print(li4[n[0]]+'-'+li1[n[1]])
                
            elif n[0]=='0':            ## unit ex 01
                print(li1[n[1]])
        else:                          ## len==1
            if n=='0':
                print('zero')
            else:
                print(li1[n])
else:
    print('ERROR')