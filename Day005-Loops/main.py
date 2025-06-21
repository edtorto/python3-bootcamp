# Loops is when something happens over and over
# 1. For loop
    # for item in item_of_lists:
    #     Do something
        
list_of_numbers = [1,2,3,4]
for number in list_of_numbers:
    # Do something
    print(number)

# 2. For loop with range
    # for number in range(a, b):
    #     # Do something
        
    # also  with step 
    # for number in range(a, b, c):
    #     # Do something
    
#  add the numbers from 1 to 100
total = 0 
for number in range(1,101):
    total += number
print(total)

# Enter a number from the user
number = int(input("Enter a number: \n"))
# using for loop and if condition with modula
total_number = 0 
for num in range (1, number+1):
    if num % 2 ==0:
        print(num)
        total_number += num
print(total_number)

# using for loop and step
even_sum = 0
for even in range(2, number+1, 2):
    even_sum += even
print(even_sum)