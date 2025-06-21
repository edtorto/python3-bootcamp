import random
# step 1
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
# step 2

guess = input("Guess a letter: ").lower()

# step 3
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong") 