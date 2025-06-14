# Note: This code checks if a given year is a leap year based on the rules defined above.
# A leap year has 366 days, with an extra day added to February (February 29). 
year = int(input("Enter a year to check if it is a leap year: \n"))
# A year is a leap year if it is divisible by 4, except for end-of-century years.
# The end-of-century year must be divisible by 400 to be a leap year.
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
