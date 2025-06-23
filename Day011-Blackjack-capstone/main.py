import random
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

user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card()) # type: ignore
    computer_cards.append(deal_card()) # type: ignore
print(user_cards) # type: ignore
print(computer_cards) # type: ignore