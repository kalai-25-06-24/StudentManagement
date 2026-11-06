students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            print("\nRoll Number:", student["roll"])
            print("Name:", student["name"])
            print("Age:", student["age"])

def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            return

    print("Student not found.")
