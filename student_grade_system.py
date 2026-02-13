students = [
    {
        "roll": 1,
        "name": "Amit",
        "marks": {"Math": 90, "Science": 88, "English": 78},
        "total": 256,
        "percentage": 85.3,
        "grade": "A"
    }
]

def students_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_students():
    roll = int(input("Enter student roll no. : "))
    name = input("Enter student name : ")
    marks = {}
    subjects = ["Math","Science","English"]
    for sub in subjects:
        while True:
            mark = int(input("enter the marks : \n"))
            if 0 <= mark <= 100:
                marks[sub] = mark
                break
            else:
                print("please enter marks between 0-100")

    total = sum(marks.values())
    percentage = total / len(subjects)
    grade = students_grade(percentage)

    students.append({"roll": roll, "name": name, "marks": marks, "total": total, "percentage": percentage, "grade" : grade})
    print("Student added successfully \n")


def view_students():
    if not students:
         print("no student record found \n")
         return

    print("-------All Students Records-------")

    for s in students:
        print(f"Roll No : {s['roll']}")
        print(f"Name : {s['name']}")
        print(f"Marks : {s['marks']}")
        print(f"Total Marks : {s['total']}")
        print(f"Percentage : {s['percentage']}")
        print(f"Grade {s['grade']}")
        print("-" * 30)

def update_students():
    subjects = ["Math","Science","English"]
    roll = int(input("Enter the roll noto update student record : "))
    for s in students:
        if s["roll"] == roll:
            new_name = input("Enter new name : ")
            s["name"] = new_name


            for sub in subjects:
                new_mark = int(input(f"enter the marks for {sub}: "))
                s["marks"][sub] = new_mark
            
            s["total"] = sum(s["marks"].values())
            s["percentage"] = s["total"] / len(subjects)
            s["grade"] = students_grade(s["percentage"])
            print("Student record updated successfully! \n")
            return
        
    print("No record found \n")

def delete_students():
    roll = int(input("Enter roll no to delete record : "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Record deleted successfully")
            return
        
    print("No record found \n")
    
def search_students():
    roll = int(input("Enter roll no to search : \n"))

    for s in students:
        if s["roll"] == roll:
            print("----Student Found----")
            print(f"Roll No : {s['roll']}")
            print(f"Name : {s['name']}")
            print(f"Marks : {s['marks']}")
            print(f"Total Marsk : {s['total']}")
            print(f"Percentage : {s['percentage']}")
            print(f"Grade {s['grade']}")
            print("-" * 30)

        
    print("No record found \n")   

while True:
    print("\n-----Student Grade System-----\n")
    print("1. Add Student")
    print("2. View Student")
    print("3. update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter Choice : ")
    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_students()
    elif choice == "4":
        delete_students()
    elif choice == "5":
        search_students()
    elif choice == "6":
        print("Exiting! GoodBye")
        break
    else:
        print("Invalid choice please enter 1-6 ")


        





