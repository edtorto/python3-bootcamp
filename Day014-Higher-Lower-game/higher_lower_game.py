from game_data import data
from art import *
import  random
from replit import clear

def format_data(account):
    """Takes the account data and returns a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user's guess and follower accounts and returns of they got it right"""
    if a_followers > b_followers:
        return  guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeatable
while game_should_continue:
    # Generate a random account
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    user_guess = input("Who has more followers? Type A or B: ").lower()

    # check if uer is correct
    # Get the follower account of each account
    a_follower_account = account_a["follower_account"]
    b_follower_account = account_b["follower_account"]

    is_correct = check_answer(user_guess, a_follower_account, b_follower_account)
    clear()
    #  Give user some feedback
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        game_should_continue = False
        print("You're wrong! Final Score: {score}")