import pickle  # Модуль для работы с файлами


class Student:
    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f"{self.last_name} {self.first_name}, возраст: {self.age}, оценки: {self.grades}"


class StudentContainer:
    def __init__(self):
        self.students = []  # Создание пустого списка студентов

    def add_student(self, student):
        self.students.append(student)  # Добавление студента в список

    def remove_student(self, student):
        self.students.remove(student)  # Удаление студента из списка

    def search_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student  # Возвращаем найденного студента
        return None  # Если студент не найден, возвращаем None

    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.students, f)  # Сохраняем список студентов в файл

    def load_from_file(self, filename):
        with open(filename, "rb") as f:
            self.students = pickle.load(f)  # Загружаем список студентов из файла


def print_menu():
    print("1. Добавить студента")
    print("2. Удалить студента")
    print("3. Найти студента")
    print("4. Вывести список всех студентов")
    print("5. Сохранить базу данных студентов в файл")
    print("6. Загрузить базу данных студентов из файла")
    print("0. Выйти")


container = StudentContainer()

while True:
    print_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        age = int(input("Введите возраст: "))
        grades = input("Введите оценки через запятую: ")
        grades = [int(x) for x in grades.split(",")]
        student = Student(first_name, last_name, age, grades)
        container.add_student(student)

    elif choice == "2":
        last_name = input("Введите фамилию студента, которого хотите удалить: ")
        student = container.search_student(last_name)
        if student:
            container.remove_student(student)
            print("Студент успешно удален")
        else:
            print("Студент не найден")

    elif choice == "3":
        last_name = input("Введите фамилию студента, которого хотите найти: ")
        student = container.search_student(last_name)
        if student:
            print(student)
        else:
            print("Студент не найден")

    elif choice == "4":
        for student in container.students:
            print(student)

    elif choice == "5":
        filename = input("Введите имя файла для сохранения: ")
        container.save_to_file(filename)
        print("База данных студентов сохранена в файл")

    elif choice == "6":
        filename = input("Введите имя файла для загрузки: ")
        container.load_from_file(filename)
        print("База данных студентов загружена из файла")

    elif choice == "0":
        break

    else:
        print("Неверный ввод")
