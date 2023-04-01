'''
This module contains a class for instantiating a game of Hangman and executing 
moves in the game; and a function for executing the game logic.
'''


import random


class Hangman:
    '''This class is used to instantiate a game of Hangman and execute moves.

    Attributes:
        word_list (list of strings): list of possible target words. 
        num_lives (int): number of lives. Decremented when player makes an incorrect guess.
        word (string): target word. Randomly selected from word_list.
        word_guessed (list of strings): correctly-guessed letters.
        num_letters (int): number of unique letters in target word which have not been guessed yet.
        list_of_guesses (list of strings): all letters guessed by player, including both correct and incorrect guesses.
    '''

    def __init__(self, word_list, num_lives=5):
        '''See help(Hangman) for accurage signature.'''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''Check player's guess against target word.

        Check if the letter guessed by player is in target word; 
        update word_guessed, num_letters and num_lives attributes;
        and display message to console to inform player if their guess
        was correct.

        Args:
            guess (str): letter guessed by player. 
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for position, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[position] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''Request and validate player input.

        Ask player to input a letter into the console. 
        If input is not a single alpha  character, or has already 
        been guessed, request input again. If input is valid, add
        it to the list_of_guesses and pass it as an argument to
        the check_guess method.
        '''
        while True:
            guess = input('Please enter a letter: ').strip()
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    '''Execute game play logic.

    Instantiate a new Hangman instance with 5 lives; keep calling its 
    ask_for_input method until the game has been won or lost. 
    Display a message to the console to inform player of the game's outcome.

    Args:
        word_list (list of strings): list of possible target words.'''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            print(f'The word is {game.word}')
            break


if __name__ == '__main__':

    word_list = ["papaya", "pineapple", "pomegranate", "pear", "starfruit"]
    play_game(word_list)
