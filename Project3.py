# Hangman Game

import random
from collections import Counter

# List of fruits
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: The word is a name of a fruit.')

    # Display underscores for the word to be guessed
    print('_ ' * len(word))

    playing = True
    letterGuessed = ''  # To store guessed letters
    chances = len(word) + 2
    flag = 0

    try:
        while chances > 0 and flag == 0:
            print()
            guess = input('Enter a letter to guess: ').lower()

            # Input validation
            if not guess.isalpha():
                print('Enter only a LETTER.')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter.')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter.')
                continue

            # Add guessed letter to the list
            letterGuessed += guess

            # If guessed letter is in the word
            if guess in word:
                print('Correct guess!')
            else:
                print('Incorrect guess!')
                chances -= 1

            # Display the word with guessed letters
            display_word = ''
            for char in word:
                if char in letterGuessed:
                    display_word += char + ' '
                else:
                    display_word += '_ '

            print(display_word.strip())

            # Check if the word is completely guessed
            if Counter(letterGuessed) == Counter(word):
                print('Congratulations, You won!')
                print('The word is:', word)
                flag = 1

        # If user runs out of chances
        if chances == 0 and Counter(letterGuessed) != Counter(word):
            print('You lost! Try again.')
            print('The word was:', word)

    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')
        exit()
