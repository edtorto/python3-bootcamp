def clear():
    """
    Clears the console screen.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')