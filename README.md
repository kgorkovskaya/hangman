# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

Created GitHub account. Created hangman repository.

## Milestone 2

Created variables for the game:
- Defined list of words.
- Chose random word from the list. 
- Asked for user input.
- Validated user input (valid input = single alpha character)

## Milestone 3

- Defined check_guess and ask_for_input functions.
- Ask_for_input requests user input and iteratively validates it. If the user enters a single alpha character, the check_guess function is called. Otherwise, a message is displayed to the console to inform the user that their input was invalid, and the user is asked to enter a single alpha charater again.
- Check_guess sets the user input to lower-case and checks if the resulting value is in the randomly-selected word. It then displays a message to the console to inform the user if their guess was correct.

## Milestone 4

- Created Hangman class
- Defined constructor method, check_guess method, and ask_for_input method.
- Constructor takes word_list as an argument, randomly selects a word from the list, calculates the number of unique letters in the word, and initializes the word_guessed and list_of_guesses attributes as empty lists, to keep track of correctly-guessed letters and all guessed letters, respectively. The num_lives attribute keeps track of the number of remaining lives and is decremented each time the user makes an incorrect guess.