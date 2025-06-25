import random
from art import logo # type: ignore
def guess_number():
    random_number = random.choice(range(1,101))
    return random_number

def check_number(random_num: int, attempt: int):
    is_attempts = True
    while attempt > 0 and is_attempts:
        print(f"You have {attempt} attempts remaining to guess the number")
        new_guess = int(input("Make a guess: "))
        if new_guess > random_num and attempt > 1:
            print("Too High.")
            print("Guess again.")
        elif new_guess < random_num and attempt > 1:
            print("Too Low.")
            print("Guess again.")
        elif new_guess > random_num or new_guess < random_num and attempt == 1:
            print("No more attempts.")
            print("You Lose!.")
        elif new_guess == random_num:
            print("You Win!.")
            is_attempts = False
        else:
            print("You Lose!.")
            is_attempts = False
        attempt -= 1 
    print(f"The random number was: {random_num}")

def guess_number_game():
    print(logo) # type: ignore
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guess = input("Guess a difficulty. Type 'easy' or 'hard': ").lower()
    random_number = guess_number()

    attempts = 10
    if  guess == 'easy':
        check_number(random_num=random_number, attempt=attempts) 

    elif guess == 'hard':
        attempts = 5
        check_number(random_num=random_number, attempt=attempts)
    else:
        print("Wrong Choice!")
            
# while input("The game has exited, Try again? 'y' or 'n' ").lower() == "y":
#     os.system('cls' if os.name == 'nt' else 'clear')
guess_number_game()