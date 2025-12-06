class Student:
    def __init__(self, student_id, student_name, dob):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__dob = dob

    def get_student_id(self):
        return self.__student_id

    def get_student_name(self):
        return self.__student_name

    def get_dob(self):
        return self.__dob

    def display_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__student_name}, Date of Birth: {self.__dob}")


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def display_info(self):
        print(f"Course ID: {self.__course_id}, Course Name: {self.__course_name}")


class StudentMarkSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks_data = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        student = Student(student_id, student_name, dob)
        self.__students.append(student)
        print("Student added successfully!\n")

    def add_course(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        self.__courses.append(course)
        print("Course added successfully!\n")

    def show_students(self):
        if not self.__students:
            print("No students to display.\n")
            return
        print("\n--- List of Students ---")
        for student in self.__students:
            student.display_info()

    def show_courses(self):
        if not self.__courses:
            print("No courses available.\n")
            return
        print("\n--- List of Courses ---")
        for course in self.__courses:
            course.display_info()

    def enter_marks(self):
        self.show_courses()
        course_id = input("Enter the course ID to input marks: ")
        if course_id not in [course.get_course_id() for course in self.__courses]:
            print("Invalid course ID.\n")
            return

        if course_id not in self.__marks_data:
            self.__marks_data[course_id] = {}

        self.show_students()
        student_id = input("Enter the student ID to input marks: ")
        if student_id not in [student.get_student_id() for student in self.__students]:
            print("Invalid student ID.\n")
            return

        try:
            mark = float(input("Enter the mark for this student: "))
            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.\n")
                return
            self.__marks_data[course_id][student_id] = mark
            print("Mark entered successfully!\n")
        except ValueError:
            print("Invalid mark input. Please enter a numeric value.\n")

    def display_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        if course_id not in self.__marks_data or not self.__marks_data[course_id]:
            print("No marks available for this course.\n")
            return

        print(f"\n--- Marks for Course {course_id} ---")
        for student in self.__students:
            student_id = student.get_student_id()
            mark = self.__marks_data[course_id].get(student_id, "Not entered")
            print(f"Student ID: {student_id}, Name: {student.get_student_name()}, Mark: {mark}")


def main():
    system = StudentMarkSystem()

    while True:
        print("\n--- MENU ---")
        print("1. Add student")
        print("2. Add course")
        print("3. Display courses")
        print("4. Display students")
        print("5. Enter marks")
        print("6. Display marks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "1":
            system.add_student()
        elif choice == "2":
            system.add_course()
        elif choice == "3":
            system.show_courses()
        elif choice == "4":
            system.show_students()
        elif choice == "5":
            system.enter_marks()
        elif choice == "6":
            system.display_marks()
        else:
            print("Invalid choice. Please try again.\n")

