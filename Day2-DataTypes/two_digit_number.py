# this program adds two digits from two digit numbers
two_digit_number = input("Enter two digit number. e.g 45 : ")
print(type(two_digit_number))
digit1 = int(two_digit_number[0])
digit2 = int(two_digit_number[1])
sum = digit1+digit2
print(sum)
# this can be done in one line of code
print(int(two_digit_number[0])+int(two_digit_number[1]))