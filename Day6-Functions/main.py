# functions in python are defined using the `def` keyword.
# A function is a block of code that only runs when it is called.
def greet(name): # type: ignore
    print(f"Hello {name}!")
# A function can take parameters, which are values that are passed into the function.
# A function can also return a value, which is a value that is returned from the function.

# while loop is used to repeat a block of code until a condition is met.
def main():
    name = input("What is your name? \n")
    greet(name)
    print("Welcome to the Python Functions tutorial!")
    while True:
        choice = input("Do you want to continue? (yes/no) \n").lower()
        if choice == "yes":
            name = input("What is your name? \n")
            greet(name)
        elif choice == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")  