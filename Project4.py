import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    # User input and validation
    choice = int(input("Enter your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please (1 to 3): '))
    
    # Mapping the user's choice to its name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")
    
    # Computer's choice
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissors'
    
    print("Computer choice is:", computer_choice_name)
    print(choice_name, 'vs', computer_choice_name)
    
    # Determining the result
    if choice == computer_choice:
        print("<== It's a tie! ==>")
    elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")
    
    # Asking the user to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")
