########################### Scope ####################

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside a function: {enemies}")

increase_enemies()
print(f"enemies outside a function: {enemies}")

# Local Scope: variable exist within a function
def drink_portion(): # type: ignore
    portion_strength = 2
    print(portion_strength)

# Global Scope: variable outside a function and its available anywhere within a file
# they are also available within a function
player_health = 10
def drink_portion():
    portion_strength = 2 # type: ignore
    print(player_health)

# Namespace: Anything you give a name too in a file is what is called a name space e.g player_health, drink_portion()

# Modifying the global variable
def increased_enemies():
    
    return enemies + 1

print(increased_enemies())

# CONSTANTS SHOULD BE IN CAPITAL LETTERS
PI =  3.14
# global variables in lower cases
name = "Edward"