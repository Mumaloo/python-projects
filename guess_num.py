import random

#want a range of numbers to guess between.
#randomly generate a number
#retrieve input number -- make sure it is a number
#if guess is wrong -- indicate if input number is too high ("your guess is too high Try again: ") or too low ("your guess is too low. Try again: ")
#if guess is right -- "Good job! You got it right!"



def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False



def guess_number():
    computer_num = random.randint(1,100)
    #print computer_num
    human_num = raw_input("Guess a number between 1 and 100: ")
    while human_num != computer_num:
        if is_number(human_num):
            #check difference between numbers
            if human_num > computer_num:
                #print human_num, computer_num
                human_num = raw_input("You guessed too high. Try a lower number: ")
            if human_num < computer_num:
                human_num = raw_input("You guessed too low. Try a higher number: ")
        else:
            human_num = raw_input("You didn't enter a number. Please enter a NUMBER between 1 and 100: ")
            # human_num = int(raw_input("Please enter a NUMBER between 1 and 100: "))
    print "Congrats! You guessed correctly!" #perhaps ask if they want to guess again with new number?





print guess_number()
#print is_number(6)