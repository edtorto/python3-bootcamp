name1 = (input("What is your name: \n"))
name2 = input("What is their name:\n")
name_combined = name1+name2
name_lower = name_combined.lower()
# count the matching letters of true
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
first_digit = t+r+u+e
# count the matching letters of love
l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
second_digit = l+o+v+e

love_score = int(str(first_digit)+str(second_digit))
# the meaning of love score
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos :) ")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")