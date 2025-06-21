# Python max function using for loop 

# Input a python list of students
student_score = input("Please enter student scores in: \n").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])  # type: ignore

highest_score = 0
for score in student_score:
    if score > highest_score: # type: ignore
        highest_score = score
print(f"Highest Score is {highest_score}")

