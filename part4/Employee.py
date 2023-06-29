class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def __init__(self, name, salary, bonus_percentage):
        super().__init__(name, salary)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        base_bonus = super().get_bonus()
        return base_bonus + self.salary * self.bonus_percentage


employee = Employee("Тимрфей", 5000)
print(employee.get_bonus())

manager = Manager("Ксения", 8000, 0.2)
print(manager.get_bonus())
