# this is a simple hangman game where the player guesses letters in a word.
# If the player guesses all letters correctly, they win.
# If they guess incorrectly, they can keep guessing until they either win or run out of lives
# This version tracks the player's lives and ends the game if they run out of lives.    

stages = [
    """
      _______
      |     |
      |     O
      |    /|\\
      |    / \\
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |    / 
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |     
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|
      |     
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |     |
      |     
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |     
      |     
      |
    __|__
    """,
    """
      _______
      |     |
      |     
      |     
      |     
      |
    __|__
    """
]
import random
# step 1
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"the chosen word is: {chosen_word}")
# step 2

word_length = len(chosen_word)
display = []

lives = 6
for _ in range(word_length):
    display += "_" # type: ignore
print(display) # type: ignore

# step 3
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter
# step 4
  if guess not in chosen_word:
      lives -= 1
      if lives == 0:
          end_of_game =True
          print("You Lose!")
  print(display) # type: ignore
  if"_" not in display:
      end_of_game = True
      print("You win!")
  print(stages[lives]) # type: ignore



