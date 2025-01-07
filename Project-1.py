# Number guessing game

import random

number_guess = random.randrange(100)

chances = 5

guess_counter = 0

while guess_counter < chances:
    
    guess_counter += 1
    my_guess = int(input("enter the number: "))
    
    if my_guess == number_guess:
        print(f"The number is {number_guess} and your guess is right ! In the {guess_counter} attempts")
        break
        
    elif guess_counter >= chances and my_guess != number_guess:
        print(f"Oops sorry, The number is {number_guess}")
        
    elif my_guess > number_guess:
        print("Guess Higher")
    
    elif my_guess < number_guess:
        print("Lower guess")