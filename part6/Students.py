import pickle

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentContainer:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def search_student_by_last_name(self, last_name):
        found_students = []
        for student in self.students:
            if student.last_name == last_name:
                found_students.append(student)
        return found_students

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.students, file)

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.students = pickle.load(file)

def main():
    container = StudentContainer()

    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student by last name")
        print("4. Save database to file")
        print("5. Load database from file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))

            student = Student(first_name, last_name, age)
            container.add_student(student)

            print("Student added successfully.")

        elif choice == "2":
            last_name = input("Enter last name of student to remove: ")

            found_students = container.search_student_by_last_name(last_name)
            if len(found_students) > 0:
                for i, student in enumerate(found_students):
                    print(f"{i+1}. {student.first_name} {student.last_name}, Age: {student.age}")
                
                index = int(input("Enter the number of the student to remove: ")) - 1
                if 0 <= index < len(found_students):
                    student = found_students[index]
                    container.remove_student(student)
                    print("Student removed successfully.")
                else:
                    print("Invalid student number.")
            else:
                print("No students found with the specified last name.")

        elif choice == "3":
            last_name = input("Enter last name of student to search: ")

            found_students = container.search_student_by_last_name(last_name)
            if len(found_students) > 0:
                for student in found_students:
                    print(f"{student.first_name} {student.last_name}, Age: {student.age}")
            else:
                print("No students found with the specified last name.")

        elif choice == "4":
            filename = input("Enter filename to save database: ")
            container.save_to_file(filename)
            print("Database saved successfully.")

        elif choice == "5":
            filename = input("Enter filename to load database from: ")
            container.load_from_file(filename)
            print("Database loaded successfully.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
