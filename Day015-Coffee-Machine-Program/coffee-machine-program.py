
def print_report(user_input, resource_dict):

    keys = list(resource_dict.keys())
    values = list(resource_dict.values())
    if user_input == 'report':
        print(f"{keys[0]}: {values[0]}ml")
        print(f"{keys[1]}: {values[1]}ml")
        print(f"{keys[2]}: {values[2]}g")
        print(f"{keys[3]}: ${values[3]}")
    return None


def check_resources():
    print("\n\n")

def process_coins():
    print("\n\n")

def check_transactions():
    print("\n\n")

def make_coffee():
    print("\n\n")


resources = {'Water': 300,
             'Milk': 200,
             'Coffee': 100,
             'Money':0.00,
             }
usr_input = input("What would you like to do?: ").lower()
print_report(user_input=usr_input, resource_dict=resources)

coffee_ingredients = [
    {
        "espresso": {
            "Water": 50,
            "Coffee": 18,
            "Money": 1.50,
            },
        "cappuccino": {
            "Water": 250,
            "Coffee": 24,
            "Milk": 100,
            "Money": 2.50,
           },
        "latte": {
            "Water": 200,
            "Coffee": 24,
            "Milk": 150,
            "Money": 3.00,
           },
    }
]

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