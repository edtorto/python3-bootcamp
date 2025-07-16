class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        """template for generating a list of values and a dictionary"""
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem("latte", water=200, milk=150, coffee=24, cost=3.0),
            MenuItem("cappuccino", water=250, milk=100, coffee=24, cost=2.5),
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a concatenated string."""
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
        otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")
        return None

