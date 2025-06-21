# fizz buz game instructions
# the program should print each number from 1 to 100
# when the number is divisible by 3 it prints Fizz
# when the number is divisible by 5 it prints Buzz
# when the number is divisible by both 3 and 5 it prints FizzBuzz
target = 100
for num in range (1, target+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    
