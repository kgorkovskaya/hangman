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
- Constructor takes word_list and num_lives as arguments (num_lives defaults to 5). It randomly selects a word from the list, sets num_letters to the number of unique letters in the word, and sets the word_guessed and list_of_guesses attributes to empty lists, to keep track of correctly-guessed letters and all guessed letters, respectively. The num_lives attribute keeps track of the number of remaining lives and is decremented each time the user makes an incorrect guess.
- The ask_for_input method uses a while loop to validate user input (valid input = single alpha character). If input is valid, it calls the check_guess method, which checks if the user's guess is in the target word by iterating over the letters in the target word. If the guess exists in the target word, the guessed letter is added to the word_guessed list, num_letters is decremented, and a message is printed to the console. If the user's guess is *not* in the target word, num_lives is decremented and a message is printed to the console. Control is then returned from the check_guess method to the ask_for_input method, which appends the user's guess to the list_of_guesses.

## Milestone 5

- Created play_game function to execute the game logic.
- This takes a list of words as an argument, and creates an instance of the Hangman class with that word list and 5 lives.
- It then executes a while loop until the game is won or lost. If the number of lives in the game is zero, the game has been lost, the loop is broken out of, and a message is printed to the console. If the number of unique, non-guessed letters in the target word is equal to zero, the game has been won, the loop is broken out of, and a message is printed to the console. If the number of lives is greater than zero and the number of unique, non-guessed letters in the target word is greater to zero, it executes the game's ask_for_input method. 