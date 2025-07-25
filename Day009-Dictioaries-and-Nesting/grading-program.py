
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Accepted"
    else:
        student_grades[student] = "Fail"
    

print(student_grades) # type: ignore
for key in student_grades: # type: ignore
    print(f"{key}: {student_grades[key]}") # type: ignore