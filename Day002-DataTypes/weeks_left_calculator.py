# This program calculates the number of weeks left until a person turns 90 years old.
# # It prompts the user to enter their current age and calculates the number of weeks left until they reach 90.
current_age = int(input("Enter your current age: \n"))
years_left = 90 - current_age
weeks_left = years_left * 52
print(f"You have approximately {weeks_left} weeks left until you turn 90.")
