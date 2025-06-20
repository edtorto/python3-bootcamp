programming_dictionary = {
    "Bug": "An error in a program that prevents a program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# creating an empty dictionary
empty_dictionary = {}

# wiping an existing empty_dictionary
# programming_dictionary = {}
# print(programming_dictionary) # type: ignore

# Edit item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer" 

# Loop through a dictionary
for key in programming_dictionary:
    # print keys
    print(key)
    print(programming_dictionary[key])