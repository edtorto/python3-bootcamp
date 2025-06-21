import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPazz Generator!")
letter_len = int(input("How many LETTERS would you like in your password? \n"))
symbols_len = int(input("How many SYMBOLS would you like in your password? \n"))
number_len = int(input("How many NUMBERS would you like in your password? \n"))

# password = ""
# for char in range(letter_len+1):  # +1 to include the last letter
#     password += random.choice(letters)
# for char in range(symbols_len+1):
#     password += random.choice(symbols)
# for char in range(number_len+1):
#     password += random.choice(numbers)
# print(f"Here is your password: {password}")

password_list = []
for char in range(letter_len+1):  # +1 to include the last letter
    password_list.append(random.choice(letters)) # type: ignore
for char in range(symbols_len+1):
    password_list.append(random.choice(symbols)) # type: ignore
for char in range(number_len+1):
    password_list.append(random.choice(numbers)) # type: ignore  
random.shuffle(password_list) # type: ignore

password = ""
for char in password_list: # type: ignore
    password += char  # type: ignore
print(f"Your password is: {password}") # type: ignore

