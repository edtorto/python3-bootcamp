# this is a simple hangman game where the player guesses letters in a word.
# If the player guesses all letters correctly, they win.
# If they guess incorrectly, they can keep guessing until they either win or run out of lives
# This version tracks the player's lives and ends the game if they run out of lives.    

import random
from hangman_art import logo, stages # type: ignore
from hangman_words import word_list # type: ignore
# step 1

chosen_word = random.choice(word_list) # type: ignore
print("Welcome to Hangman game")
print(logo[0]) # type: ignore
print(f"The chosen word has: {len(chosen_word)} letters")
# step 2

word_length = len(chosen_word) # type: ignore
display = []

lives = 6
for _ in range(word_length):
    display += "_" # type: ignore
print(display) # type: ignore

# step 3
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position] # type: ignore
        if letter == guess:
            display[position] = letter
    # step 4
    if guess not in chosen_word:
        print(f"You have guessed {guess}, that's not in the word.\n You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game =True
            print("You Lose!")
            print(f"The chosen word was: {chosen_word}")
    print(display) # type: ignore
    if"_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives]) # type: ignore





