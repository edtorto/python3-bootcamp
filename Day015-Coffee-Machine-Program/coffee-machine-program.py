
def print_report(user_input, resource_dict):

    keys = resource_dict.keys()
    values = resource_dict.values()
    if user_input == 'report':
        print(f"{keys[0]}: {values[0]}ml")
        print(f"{keys[1]}: {values[1]}ml")
        print(f"{keys[2]}: {values[2]}g")
        print(f"{keys[3]}: ${values[3]}")
    return None


def check_resources(drink_name):
    if drink_name in MENU:
        details = MENU[drink_name]
        for item, amount in details["ingredients"].items():
            print(f"{item}: {amount}")
        print(f"cost: {details['cost']}")
    else:
        print("Sorry, that drink is not on the menu.")

def process_coins():
    print("\n\n")

def check_transactions():
    print("\n\n")

def make_coffee():
    print("\n\n")


resources = {'water': 300,
             'milk': 200,
             'coffee': 100,
             }

# usr_input = input("What would you like to do?: ").lower()
# print_report(user_input=usr_input, resource_dict=resources)

MENU = {
        "espresso": {
            "ingredients":{
            "water": 50,
            "coffee": 18,
        }, "cost": 1.50,
    },
        "cappuccino": {
            "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
           },"cost": 2.50,
    },
        "latte": {
            "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
           },"cost": 3.00,
    },
}


# print(f"{MENU[""]}: {values[0]}ml")
# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
print(check_resources(user_choice))
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