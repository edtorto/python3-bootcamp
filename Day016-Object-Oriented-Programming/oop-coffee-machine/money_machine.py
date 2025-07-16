class MoneyMachine:

    def __init__(self):
        self.profit = 0.00

    def process_coins(self):
        """Returns the total calculated from the inserted coins."""
        print("Please insert the coins:")
        total = int(input("how many quarters: ")) * 0.25
        total += int(input("how many dimes: ")) * 0.10
        total += int(input("how many nickels: ")) * 0.05
        total += int(input("how many pennies: ")) * 0.01
        return total

    def make_payment(self, drink_cost):
        """Return True when the payment is accepted, or False when the money is insufficient."""
        money_received = self.process_coins()
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def report(self):
        print(f"Money: ${self.profit:.2f}")
        return None
