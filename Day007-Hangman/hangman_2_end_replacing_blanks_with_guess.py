import random
# step 1
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"the chosen word is: {chosen_word}")
# step 2

word_length = len(chosen_word)
display = []

for _ in range(word_length):
    display += "_" # type: ignore
print(display) # type: ignore

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display) # type: ignore