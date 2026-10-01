students = []
ids = 1
def add_Student(name:str, mark:int):
    global ids
    students.append({"id" : ids ,"name": name, "mark": mark})
    ids +=1

def view_student():

    if len(students) == 0:
        print("No Student Details present")
    for std in students:
        print(f"{std['name']}: marks: {std['mark']}")

def search_by_id(id:int):

    if len(students) == 0:
        print("No Student Details present")
        return None

    for ind in range(len(students)):
        std = students[ind]
        if std['id'] == id:
            return (std, ind)
        
    return None,None


def update_student(id: int, mark: int = None):
    std,ind = search_by_id(id)
    if std == None:
        print("NO Student Details present with this id")
        return False
    std["mark"] = mark
    students[ind] = std
    return True


def delete_student(id:int = None):

    if id:
        std,ind = search_by_id(id)
        if std == None:
            return False
        students.pop(ind)
        return True


def class_avg_marks():
    if len(students) == 0:
        print("No Student Details Data Present")
        return None
    sum = 0
    for std in students:
        sum += std["mark"]
    
    return sum / len(students)


def topper():
    if len(students) == 0:
        print("No Student Details Data Present")
        return None
    max = -1
    student = None
    for std in students:
        # sum += std["mark"]
        if max < std["mark"]:
            max = std["mark"]
            student = std

    
    return student


while True:

        print("== Welcome to Student Portal ===")
        print("1. Add Student Detail")
        print("2. View All Students")
        print("3. Search Student BY Id")
        print("4. Update Student Detail")
        print("5. Delete Student Data")
        print("6. Get Class Avg Mark")
        print("7. Get Highest Performing Student Details")
        print("8. Exit")
        print()
        print()

        choice = int(input("Choose Option between 1 to 8"))
        if choice == 1:
            name = input("Enter Student Name")
            mark = int(input("Enter Student mark"))
            if mark < 0:
                print("Mark is less than zero. Please choose correct option")
                continue

            add_Student(name,mark)
        elif choice == 2:
            view_student()

        elif choice == 3:
            id = int(input("Enter Student Id"))
            std, ind = search_by_id(id)
            if std:
                print(f"{std['name']}: marks: {std['mark']}")

        elif choice == 4:
            id = int(input("Enter Student Id whose mark need to update"))
            mark = int(input("Enter Student mark to update"))
            is_updated = update_student(id,mark)
            if is_updated:
                print(f"Mark updated for student id : {id}")
 

        elif choice == 5:
            id = int(input("Enter Student Id whose data need to delete"))
            is_deleted = delete_student(id)
            if is_deleted:
                print(f"Student Data Deleted for id : {id}")

        elif choice == 6:
            avg_mark = class_avg_marks()
            if avg_mark is not None:
                print(f"Avg Amrk of class is : {avg_mark}")

        elif choice == 7:
            std = topper()
            if std is not None:
                print(f"{std['name']}: marks: {std['mark']}")

        elif choice == 8:
            break

