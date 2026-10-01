marks = [98,56,79,45,83]

def student_grade(marks:list[int]):
    total = 0
    percentage = 0
    for mark in marks:
        total +=mark

    percentage = total / (len(marks) * 100) * 100

    if percentage < 40:
        return "FAIL"
    elif percentage < 60:
        return "Grade D"
    elif percentage < 70:
        return "Grade C"
    elif percentage < 85:
        return "Grade B"
    else:
        return "Grade A"
    
grade = student_grade(marks)
print(grade)
