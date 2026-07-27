import csv
import os

file_name = "students.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course"])


# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course])

    print("\nStudent Added Successfully!\n")


# View Students
def view_students():
    print("\n------ Student Records ------")

    with open(file_name, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print("{:<10} {:<20} {:<10} {:<15}".format(row[0], row[1], row[2], row[3]))

    print()


# Search Student
def search_student():
    student_id = input("Enter Student ID to Search: ")

    found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[0] == student_id:
                print("\nStudent Found")
                print("ID     :", row[0])
                print("Name   :", row[1])
                print("Age    :", row[2])
                print("Course :", row[3])
                found = True
                break

    if not found:
        print("\nStudent Not Found!\n")


# Update Student
def update_student():
    student_id = input("Enter Student ID to Update: ")

    rows = []
    found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[0] == student_id:
                print("\nEnter New Details")
                row[1] = input("Name: ")
                row[2] = input("Age: ")
                row[3] = input("Course: ")
                found = True

            rows.append(row)

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("\nStudent Updated Successfully!\n")
    else:
        print("\nStudent ID Not Found!\n")


# Delete Student
def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    rows = []
    found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[0] == student_id:
                found = True
            else:
                rows.append(row)

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("\nStudent Deleted Successfully!\n")
    else:
        print("\nStudent ID Not Found!\n")


# Main Menu
while True:

    print("=================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.\n")
