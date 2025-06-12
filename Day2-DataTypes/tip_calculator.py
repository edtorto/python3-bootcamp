# this program calculates the tip amount based on the total bill and the percentage of the tip.
# It prompts the user to enter the total bill amount and the tip percentage, then calculates and displays the tip amount.
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill?\n "))
tip_percentage = tip/100
tip_amount=(total_bill/people) *(1+ tip_percentage) 
# print(f"tip percentage {tip_percentage} and tip amount {tip_amount}")
print(f"Each person should pay: ${tip_amount:.2f}")
