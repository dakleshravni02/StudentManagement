# Initialize data structures
students = {}  # Dictionary to store student records with ID as key
student_ids = []  # List to keep track of student IDs

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade: ")
    
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = (name, age, grade)
        student_ids.append(student_id)
        print("Student record added successfully!")

def view_students():
    if not students:
        print("No student records found!")
    else:
        for student_id in student_ids:
            name, age, grade = students[student_id]
            print(f"ID: {student_id}, Name: {name}, Age: {age}, Grade: {grade}")

def search_student():
    search_id = input("Enter Student ID to search: ")
    search_result = students.get(search_id, None)

    if search_result:
        name, age, grade = search_result
        print(f"Search Result - ID: {search_id}, Name: {name}, Age: {age}, Grade: {grade}")
    else:
        print("Student not found!")

def update_student():
    update_id = input("Enter Student ID to update: ")
    if update_id in students:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        grade = input("Enter New Grade: ")
        students[update_id] = (name, age, grade)
        print("Student record updated successfully!")
    else:
        print("Student ID not found!")

def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    if delete_id in students:
        students.pop(delete_id)
        student_ids.remove(delete_id)
        print("Student record deleted successfully!")
    else:
        print("Student ID not found!")

def exit_program():
    print("Exiting program...")
    exit()

# Menu loop
while True:
    print("\nMenu:")
    print("1. Add Student Record")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Information")
    print("5. Delete Student Record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            add_student()
        case '2':
            view_students()
        case '3':
            search_student()
        case '4':
            update_student()
        case '5':
            delete_student()
        case '6':
            exit_program()
        case _:
            print("Invalid choice! Please enter a valid option.")