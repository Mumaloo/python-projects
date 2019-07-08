import random

def dice_roll(sides):
    numRolled = random.randint(1, sides)
    return numRolled
    
    
def choice():
    roll = True
    while roll == True:
        is_rolled = raw_input("Would you like to roll the die? ENTER=Roll. Q=Quit. ")
        if is_rolled.lower() != "q":
            print dice_roll(6)
        else:
            roll = False
            print "Thanks for playing!"

    

print choice()



