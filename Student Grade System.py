# Simple Student Grade System

students = {}

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []
    subjects = ["Math", "Science", "English"]

    for subject in subjects:
        mark = float(input(f"Enter {subject} mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    students[roll_no] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    print("\nStudent added successfully!\n")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for roll_no, data in students.items():
        print("\nRoll No:", roll_no)
        print("Name:", data["Name"])
        print("Marks:", data["Marks"])
        print("Total:", data["Total"])
        print("Average:", round(data["Average"], 2))
        print("Grade:", data["Grade"])


def search_student():
    roll_no = input("Enter roll number to search: ")

    if roll_no in students:
        data = students[roll_no]

        print("\nStudent Found")
        print("Name:", data["Name"])
        print("Marks:", data["Marks"])
        print("Average:", round(data["Average"], 2))
        print("Grade:", data["Grade"])
    else:
        print("Student not found.")


def main():
    while True:
        print("\n===== Student Grade System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


main()