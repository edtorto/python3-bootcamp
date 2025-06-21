# A year is a leap year if it is divisible by 4, except for end-of-century years.
# The end-of-century year must be divisible by 400 to be a leap year.

from calendar import month


def is_leap(year: int): # type: ignore
    """checks if its a leap year or not

    Args:
        year (int): number of a year

    Returns:
        boolean: True or False
    """
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year: int, month: int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month -1]

year = int(input("Enter a year: \n"))
month = int(input("Enter a month: \n"))
days = days_in_month(year, month)
print(f"The're  number of {days} days in {month} month of {year}")