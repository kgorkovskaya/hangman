import random
import re

word_list = ["papaya", "pineapple", "pomegranate"]
word = random.choice(word_list)

guess = input('Enter a letter: ').strip().lower()
if re.match('^[a-z]$', guess):
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
