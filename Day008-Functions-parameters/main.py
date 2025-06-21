# Today we are going to learn about functions and parameters in Python.
def greet(): # type: ignore
    """Function to greet a person with their name."""
    print(f"Hello, Edward!")    

# Calling the function with a name
greet()

#  function that allows input
def greet_with_name(name): # type: ignore
    """Function to greet a person with their name."""
    print(f"Hello, {name}!")    

# Calling the function with a name
greet_with_name("Alice")

# function with more than 1 input
def greet_with(name, location): # type: ignore
    print(f"Hello {name}!")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")

# function with keyword arguments
def greet_with(name: str="Edward", location: str="Uganda"):
    print(f"Hello {name}!")
    print(f"What is it like in {location}")
greet_with()


# paint can calculator
# import math
# def paint_calc(height: int, width: int, cover: int = 5):
#     number_of_cans = (height*width) / cover
#     round_up = math.ceil(number_of_cans) # type: ignore
#     print(f"You will need {round_up} cans of paint.") # type: ignore
# test_h = int(input(f"What is the height in meters: \n"))
# test_w = int(input(f"What is the width in meters: \n"))
# # coverage = 5
# paint_calc(height = test_h, width = test_w) # type: ignore

# prime number calculator
def prime_checker(number: int):
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
        
n = int(input(f" Enter an integer between 2 and 100:\n"))
prime_checker(number=n)