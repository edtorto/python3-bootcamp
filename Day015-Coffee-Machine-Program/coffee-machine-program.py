def check_resources(order_ingredients):
    """Returns True when the order can be made, and False when the resources are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, that's not enough {item}!")
            return False
        return True
    return None

def process_coins():
    """Returns the total calculated from the inserted coins."""
    print("Please insert the coins: ")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nicks: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total

def check_transactions(money_received, drink_cost):
    """Return True when the payment is accepted, of False when the money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change}  in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name ,order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

resources = {'water': 300,
             'milk': 200,
             'coffee': 100,
             }
profit = 0.00

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

is_on = True

while is_on:
    # Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee': {resources['coffee']}g")
        print(f"cost: ${profit}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_transactions(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])