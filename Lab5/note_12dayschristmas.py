def note(x,count):
        while count>=0:
                if x==1:
                        print("On the first day of Christmas, my true love sent to me:")
                elif x==2:
                        print("On the second day of Christmas, my true love sent to me:")            
                elif x==3:
                        print("On the third day of Christmas, my true love sent to me:")
                elif x==4:
                        print("On the fourth day of Christmas, my true love sent to me:")
                elif x==5:
                        print("On the fifth day of Christmas, my true love sent to me:")
                elif x==6:
                        print("On the sixth day of Christmas, my true love sent to me:")
                elif x==7:
                        print("On the seventh day of Christmas, my true love sent to me:")
                elif x==8:
                        print("On the eighth day of Christmas, my true love sent to me:")
                elif x==9:
                        print("On the ninth day of Christmas, my true love sent to me:")
                elif x==10:
                        print("On the tenth day of Christmas, my true love sent to me:")
                elif x==11:
                        print("On the eleventh day of Christmas, my true love sent to me:")
                elif x==12:
                        print("On the twelfth day of Christmas, my true love sent to me:")
        
                if count==1:
                        if x==1:
                                print("A Partridge in a Pear Tree.")
                        else:
                                print("And a Partridge in a Pear Tree.")
                if count==2:  
                        print("Two Turtle Doves,")
                if count==3:
                        print("Three French Hens,")
                if count==4:
                        print("Four Calling Birds,")
                if count==5:
                        print("Five Golden Rings,")
                if count==6:
                        print("Six Geese a Laying,")
                if count==7:
                        print("Seven Swans a Swimming,")
                if count==8:
                        print("Eight Maids a Milking,")
                if count==9:
                        print("Nine Ladies Dancing,")
                if count==10:
                        print("Ten Lords a Leaping,")
                if count==11:
                        print("Eleven Pipers Piping,")
                if count==12:
                        print("Twelve Drummers Drumming,")
                x=x-count
                count=count-1        

count=0
while count>=0:
        x=int(input("Enter day (1 to 12, 0 to quit): "))
        
        if x==0:
                break
        elif x>12 or x<1:
                print('Day is out of range.')        
        else:
                count=x
                note(x,count)
        
        
        


       
        