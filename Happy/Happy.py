#program tests if an integer is "happy"

def sumSquareDigits(num): 
    total = 0 
    for digit in num:
        square = int(digit) ** 2
        total += square
    return total

while True:
    while True:
        try:
            number = int(input("Enter an integer to test if happy: "))
            break
        except ValueError:
            print("Not an integer!")

    happy = number
    happyValues = [happy]
    while happy != 1:
        happy = sumSquareDigits(str(happy))
        print(happy)
        if happy in happyValues:
            break
        else:
            happyValues.append(happy)

    if happy == 1:
        print(number, "is happy! :)")
    else:
        print(number, "is unhappy! :(")


    





        


        
            

    
