# this program calculates the BMI (Body Mass Index) of a person
weight = int(input("Enter your weight in kg. e.g 65: \n"))
height = float(input("Enter your height in meters. e.g 1.72:\n "))
bmi = int(weight / (height ** 2))

# Note: The BMI categories are based on the World Health Organization (WHO) classification.
if bmi < 18.5:
    print(f"Your Body Mass Index (BMI) is: {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your Body Mass Index (BMI) is: {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your Body Mass Index (BMI) is: {bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your Body Mass Index (BMI) is: {bmi}. You are obese.")
else:
    print(f"Your Body Mass Index (BMI) is: {bmi}. You are clinically obese.")
