import random
import os
from art import logo # type: ignore
################### The Blackjack House Rules #######################
## 1. The deck is unlimited in size
## 2. There are no Jokers
## 3. The Jack/King/Queen all count as 10
## 4. The Ace can count as 1 or 11
## 5. Use the following as the following list as th deck of cards:

## 6. The cards in the card have equal probability of being drawn
## 7. Cards are not removed from the deck as they are being drawn

def deal_card(): # type: ignore
    """Returns a random card from the deck.

    Returns:
        int: random card number
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards) # type: ignore
    return card # type: ignore

def calculate_score(cards): # type: ignore
    """Takes the lost of cards and calculate the scores od cards.

    Args:
        cards (list): List of card values.

    Returns:
        int: Calculated score.
    """
    score = sum(cards) # type: ignore
    if score == 21 and len(cards) == 2: # type: ignore
        return 0 # Blackjack
    if 11 in cards and score > 21:
        cards.remove(11) # type: ignore
        cards.append(1) # type: ignore
    return sum(cards)  # type: ignore

def compare(user_score, computer_score): # type: ignore
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has a blackjack"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "Opponent went over, You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo) # type: ignore
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card()) # type: ignore
        computer_cards.append(deal_card()) # type: ignore
    print(user_cards) # type: ignore
    print(computer_cards) # type: ignore

    while not is_game_over:
        user_score = calculate_score(cards=user_cards) # type: ignore
        computer_score = calculate_score(cards=computer_cards) # type: ignore
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Fist computer card: {computer_cards}, computer score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score == 21: # type: ignore
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card()) # type: ignore
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17: # type: ignore
        
        print(f"Your final hand: {user_cards}, final score: {user_score}") # type: ignore
        print(f"Computer hand: {computer_cards}, computer score: {computer_score}") # type: ignore
        print(compare(user_score=user_score, computer_score=computer_score)) # type: ignore

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower() == "y":
    os.system('cls' if os.name == 'nt' else 'clear')

    play_game()