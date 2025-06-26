####################Debugging Exercise####################
# 1. Describe the problem:
# The code is supposed to calculate the average of a list of numbers, but it is not
# returning the correct result. 
# - What is the expected output? The expected output is the average of the numbers in the list.
# - What is the actual output? The actual output is not the average of the numbers in the list.
# - What is the error message? There is no error message, but the output is not as expected. 
# - What is the line number where the error occurs? The error occurs in the line where the average is calculated.
# - What is the type of error? The error is a logical error, not a syntax error. 
# 2. Reproduce the bug:
# The bug can be reproduced by running the code with the provided list of numbers.
#3. Play the computer:
# The code is supposed to calculate the average of a list of numbers, but it is not
# returning the correct result.
# 4. Fix the bug:
# The bug is in the calculation of the average. The sum of the numbers is divided by
# the length of the list, but the length is not being calculated correctly. 
def calculate_average(numbers): # type: ignore
    total = sum(numbers) # type: ignore
    count = len(numbers) # type: ignore
    average = total / count
    return average
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average of {numbers} is {average}") 
# 5. Print is your friend:
print(f"Total: {sum(numbers)}, Count: {len(numbers)}, Average: {average}")
# 6. Use a debugger:
# The code runs correctly, but we can use a debugger to step through the code and
# inspect the values of `total`, `count`, and `average` at each step.
# pythontutorial.com/debugging-in-python/
# thonn.org/doc/tutorial/debugging.html
# 7. Take a break:
# Taking a break can help clear your mind and give you a fresh perspective on the problem.
# 8. talk to a friend:
# Explaining the code to a friend can help clarify the logic and identify any mistakes.
# 9. Run the code again:
# The code runs correctly now and returns the expected output.
# 10. ask stack overflow:
# If the problem persists, you can ask for help on Stack Overflow with a clear description
# of the issue, the expected output, and the actual output.
