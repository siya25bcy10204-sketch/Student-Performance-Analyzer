students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks (0–100): "))
    
    # Simple AI-like rule-based prediction
    if marks >= 90:
        performance = "Excellent"
    elif marks >= 75:
        performance = "Good"
    elif marks >= 50:
        performance = "Average"
    else:
        performance = "Poor"
    
    student = {
        "name": name,
        "marks": marks,
        "performance": performance
    }
    
    students.append(student)
    print("\nStudent added successfully!\n")


def show_students():
    if len(students) == 0:
        print("\nNo students found!\n")
        return
    
    print("\n------ Student Records ------")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Predicted Performance: {s['performance']}")
        print("-----------------------------")
    print()


def search_student():
    name = input("Enter student name to search: ")
    found = False
    
    for s in students:
        if s["name"].lower() == name.lower():
            print("\n---- Student Found ----")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Performance: {s['performance']}")
            print("-----------------------\n")
            found = True
            break
    
    if not found:
        print("\nStudent not found.\n")


def menu():
    while True:
        print("========= STUDENT PERFORMANCE ANALYZER =========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        print("===============================================")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("\nExiting Program... Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Try again.\n")


# Run the program
menu()
