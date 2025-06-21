# calculator

# add
def add(n1, n2): # type: ignore
    return n1+n2 # type: ignore

# subtract
def subtract(n1, n2): # type: ignore
    return n1-n2 # type: ignore

# multiply
def multiply(n1, n2): # type: ignore
    return n1*n2 # type: ignore

# divide
def divide(n1, n2): # type: ignore
    return n1 / n2 # type: ignore

# operations
operations = { # type: ignore
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number: \n"))

    for symbol in operations:
        print(symbol) # type: ignore
    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: \n")

        num2 = float(input("What is the next number: \n"))

        calculation_function = operations[operations_symbol] # type: ignore
        answer = calculation_function(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        choice = input("Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ").lower() 
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()
