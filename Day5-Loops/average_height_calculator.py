# Input a python list of students
student_heights = input("Please enter student heights in cm: \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # type: ignore

total_height = 0
for height in student_heights:
    total_height += height  # type: ignore
print(f"Total height = {total_height}")

# python len function
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"The number of students =  {number_of_students}")

average_height = round(total_height / number_of_students) # type: ignore
print(f"Average height = {average_height}\n")