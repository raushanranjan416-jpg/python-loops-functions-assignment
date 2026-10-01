marks =  [85, 92, 78, 88, 95, 35, 17, 99, 45, 60]


def mark_analyzer(marks:list[str]):
    avg_mark = 0
    highest_mark = 0
    pass_student_count = 0
    failed_student_count = 0
    lowest_mark = 100

    for mark in marks:
        if mark > 40:
            pass_student_count +=1
        else:
            failed_student_count +=1
        
        if mark < lowest_mark:
            lowest_mark = mark
        
        if mark > highest_mark:
            highest_mark = mark
        
        avg_mark += mark

    return f"Avg mark : {avg_mark/len(marks)}, Highest mark: {highest_mark}, lowest mark : {lowest_mark}, Student Pass Count : {pass_student_count}, Student Failed Count: {failed_student_count}"


print(mark_analyzer(marks))