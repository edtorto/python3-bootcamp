
resources = {'Water': 1000,
             'Coffee': 500,
             'Milk': 1500,
             'Money':0.00,
             }
coffee_ingredients = [
    {
        "espresso": {
            "Water": 100,
            "Coffee": 75,
            "Milk": 100,
            "Money": 2.50,
            },
        "cappuccino": {
            "Water": 100,
            "Coffee": 100,
            "Milk": 200,
            "Money": 3.00,
           },
        "latte": {
            "Water": 100,
            "Coffee": 50,
            "Milk": 150,
            "Money": 2.00,
           },
    }
]
print(coffee_ingredients[0]['espresso']['Water'])

# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
## Check the user’s input to decide what to do next.
if user_choice == "espresso":
    print("Enjoy")
elif user_choice == "latte":
    print("Ready")
elif user_choice == "cappuccino":
    print("Ok")
else:
    print("Sorry, Wrong Choice! Choose from the options.")
## The prompt should show every time action has completed and again to serve the next customer.

#  Turn off the Coffee Machine by entering “ off ” to the prompt.

#  Print report.

# Check resources sufficient?
## check if there are enough resources to make that drink.
## It should not continue to make the drink for insufficient resources

# prompt the user to insert coins.

#  Check transaction successful?
# Check that the user has inserted enough money to purchase the drink they selected.
## If not enough refund the Money .
## But if the user has inserted enough money, make coffee and a report
## If the user has inserted too much money, the machine should offer change, coffee and report.

#  Make Coffee.

## If the transaction is successful and there are enough resources make coffee, offer a report before and after
## Serve Coffe