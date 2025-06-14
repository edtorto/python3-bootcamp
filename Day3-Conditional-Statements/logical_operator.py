# this program checks if you can go for a roller coaster or not (elif statement)
print("welcome to the Rollercoaster!")
height = int(input("what is your height in cm?\n"))
bill = 0
if height >= 140:
    print("You can ride a rollercoaster")
    age = int(input("what is your age?\n"))
    if age  <= 12:
        bill  = 7
        print("You are paying $7")
    elif age  < 18:
        bill = 14
        print("You are paying $14")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is free")
    else:
        bill = 21
        print("You are paying $21")
    wants_a_photo = input("Do you want a photo taken? Y or N\n")
    if wants_a_photo == "Y":
        bill += 5   
        print("You are paying an additional $5 for the photo")
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller to ride the rollercoaster")