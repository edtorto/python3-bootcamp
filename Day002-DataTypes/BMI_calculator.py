# this program calculates the BMI (Body Mass Index) of a person
weight_as_int = int(input("Enter your weight in kg. e.g 65: \n"))
height_as_float = float(input("Enter your height in meters. e.g 1.72:\n "))
bmi = int(weight_as_int / (height_as_float ** 2))
print(f"Your Body Mass Index (BMI) is: {bmi}")