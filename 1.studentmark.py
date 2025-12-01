def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return {"id": student_id, "name": student_name, "dob": dob}

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_students():
    student_list = []
    number_of_students = int(input("Enter the number of students: "))
    for i in range(number_of_students):
        student = input_student_info()
        student_list.append(student)
    return student_list

def input_courses():
    course_list = []
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course = input_course_info()
        course_list.append(course)
    return course_list

def display_courses(course_list):
    print("\n--- List of Courses ---")
    for course in course_list:
        print(f"ID: {course['id']}, Name: {course['name']}")

def display_students(student_list):
    print("\n--- List of Students ---")
    for student in student_list:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def input_marks(student_list, course_list, marks_data):
    display_courses(course_list)
    course_id = input("Enter the course ID to input marks: ")
    if course_id not in [course['id'] for course in course_list]:
        print("Invalid course ID.")
        return

    if course_id not in marks_data:
        marks_data[course_id] = {}

    display_students(student_list)
    student_id = input("Enter the student ID to input marks: ")
    if student_id not in [student['id'] for student in student_list]:
        print("Invalid student ID.")
        return

    try:
        mark = float(input("Enter mark: "))
        marks_data[course_id][student_id] = mark
    except ValueError:
        print("Invalid mark input. Please enter a numeric value.")

def display_marks(student_list, marks_data):
    course_id = input("Enter the course ID to view marks: ")
    if course_id not in marks_data or not marks_data[course_id]:
        print("No marks available for this course.")
        return

    print(f"\n--- Marks for Course {course_id} ---")
    for student in student_list:
        student_id = student["id"]
        mark = marks_data[course_id].get(student_id, "Not entered")
        print(f"Student ID: {student_id}, Name: {student['name']}, Mark: {mark}")

# Main
def main():
    student_list = []
    course_list = []
    marks_data = {}

    while True:
        print("\n--- MENU ---")
        print("1. Input students")
        print("2. Input courses")
        print("3. Display courses")
        print("4. Display students")
        print("5. Input marks")
        print("6. Display marks")
        print("0. Exit program")

        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "1":
            student_list = input_students()
        elif choice == "2":
            course_list = input_courses()
        elif choice == "3":
            display_courses(course_list)
        elif choice == "4":
            display_students(student_list)
        elif choice == "5":
            input_marks(student_list, course_list, marks_data)
        elif choice == "6":
            display_marks(student_list, marks_data)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()