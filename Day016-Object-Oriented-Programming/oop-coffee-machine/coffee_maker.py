class CoffeeMaker:
    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
        }
    def report(self):
        """Prints a report of the resources"""
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}ml")
        print(f"coffee: {self.resources['coffee']}g")

    def is_resource_insufficient(self, order_ingredients):
        """Returns True when the order can be made, and False when the resources are insufficient"""
        for item in order_ingredients:
            if order_ingredients[item] >= self.resources.get(item, 0):
                print(f"Sorry, there's not enough {item}!")
                return False
            return True
        return None

    def make_coffee(self, drink_name, order_ingredients):
        """Deduct the required ingredients from the resources"""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}. Enjoy!")