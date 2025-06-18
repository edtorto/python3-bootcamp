# Today we are going to learn about functions and parameters in Python.
def greet(name): # type: ignore
    """Function to greet a person with their name."""
    print(f"Hello, {name}!")    

# Calling the function with a name
greet("Alice")