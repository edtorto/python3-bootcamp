# Clear the screen
import os


def clear() -> None:
    """
    :rtype: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
