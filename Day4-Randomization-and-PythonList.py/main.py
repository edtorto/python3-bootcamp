# # 1. randomization (deterministic or pseudo randomization)
# import random

# random_number = random.randint(1, 100)
# print(random_number)
# # Random float between 0.0 and 1.0
# random_float = random.random()
# print(random_float)
# # Random float between 1.0 and 10.0
# random_float_between_1_and_10 = random.uniform(1.0, 10.0)
# print(random_float_between_1_and_10)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# 2. list
fruits = ["apple","mangos","oranges"]
print(fruits[1])
fruits.append("grapes")
print(fruits.index("apple"))
fruits[0] = "Apples"
print(fruits)
print(len(fruits))

# names = ["Angela", "Ben", "Jenny", "Micheal", "Chloe"]
# # get the random numbers between zero and the last index 
# name_index = random.randint(0, (len(names)-1))
# print(f"{names[name_index]} is going to buy a meal today!")

# 3. Nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]