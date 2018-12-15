hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))

import math

def calculate_parking_fee(hours, minutes):
    total_minute = minutes + (hours * 60)
    time = math.ceil(total_minute/60)
    total_minute = time * 60
    fee  = 0
    if(total_minute > (20*60) or hours < 0 or hours > 20 or minutes < 0 or minutes > 59):
        print("Invalid time.")
    else:
        
        if buyAmt >= 3001:
            print("No charge, thank you.")
        else:
            if(total_minute <= (2*60)):
                print("No charge, thank you.")
            elif(total_minute >= (3*60) and total_minute <= (4*60)):
                if(buyAmt >= 300 and buyAmt <= 3000):
                    print("No charge, thank you.")
                else:
                    if total_minute > (60*3):
                        fee = 40
                    else:
                        fee = 20
                    print("Total amount due is %d Baht, thank you."%(fee))
            elif total_minute >= (5*60):
                fee = 50 * math.ceil(total_minute/60)
                fee -= 100
                if(buyAmt >= 300):
                    fee -= 100
                else:
                    fee -= 60
                print("Total amount due is %d Baht, thank you.."%(fee))
    
calculate_parking_fee(hours, minutes)      
