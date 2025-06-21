# this program checks if you can go for a roller coaster or not (ifelse statement)
print("------------------------------------------------")
print("         nested ifelse statement")
print("------------------------------------------------")
print("welcome to the Rollercoaster!")
height = int(input("what is your height in cm?\n"))
if height >= 140:
    print("You can ride a rollercoaster")
else:
    print("Sorry, you have to grow taller to ride the rollercoaster")
    
# this program checks if you can go for a roller coaster or not (nested ifelse statement)
print("------------------------------------------------")
print("                ifelse statement")
print("------------------------------------------------")
print("welcome to the Rollercoaster!")
height = int(input("what is your height in cm?\n"))
if height >= 140:
    print("You can ride a rollercoaster")
    age = int(input("what is your age?\n"))
    if age  >= 18:
        print("You are paying $7")
    else:
        print("You are paying $14")
else:
    print("Sorry, you have to grow taller to ride the rollercoaster")
print("------------------------------------------------")
print("                elif statement")
print("------------------------------------------------")
# this program checks if you can go for a roller coaster or not (elif statement)
print("welcome to the Rollercoaster!")
height = int(input("what is your height in cm?\n"))
if height >= 140:
    print("You can ride a rollercoaster")
    age = int(input("what is your age?\n"))
    if age  <= 12:
        print("You are paying $7")
    elif age  < 18:
        print("You are paying $14")
    else:
        print("You are paying $21")
else:
    print("Sorry, you have to grow taller to ride the rollercoaster")