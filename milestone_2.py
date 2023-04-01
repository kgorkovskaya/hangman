import random

word_list = ["papaya", "pineapple", "pomegranate", "pear", "starfruit"]
word = random.choice(word_list)

guess = input('Enter a letter: ').strip().lower()
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
