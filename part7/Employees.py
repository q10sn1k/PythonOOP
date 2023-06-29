import pickle

class Employee:
    def __init__(self, first_name, last_name, age, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.position}, Salary: {self.salary}"

class EmployeeContainer:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        self.employees.remove(employee)
    
    def search_by_lastname(self, last_name):
        return [employee for employee in self.employees if employee.last_name == last_name]
    
    def search_by_position(self, position):
        return [employee for employee in self.employees if employee.position == position]
    
    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary
    
    def get_highest_salary_employee(self):
        highest_salary_employee = max(self.employees, key=lambda employee: employee.salary)
        return highest_salary_employee
    
    def get_lowest_salary_employee(self):
        lowest_salary_employee = min(self.employees, key=lambda employee: employee.salary)
        return lowest_salary_employee
    
    def save_employees(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.employees, file)
    
    def load_employees(self, filename):
        with open(filename, 'rb') as file:
            self.employees = pickle.load(file)

def print_menu():
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Search by Last Name")
    print("4. Search by Position")
    print("5. Calculate Total Salary")
    print("6. Get Employee with Highest Salary")
    print("7. Get Employee with Lowest Salary")
    print("8. Save Employees to File")
    print("9. Load Employees from File")
    print("0. Exit")

employee_container = EmployeeContainer()

while True:
    print_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        position = input("Enter position: ")
        salary = float(input("Enter salary: "))
        
        employee = Employee(first_name, last_name, age, position, salary)
        employee_container.add_employee(employee)
        print("Employee added successfully!")
    
    elif choice == "2":
        last_name = input("Enter last name of the employee to remove: ")
        employees_to_remove = employee_container.search_by_lastname(last_name)
        
        if len(employees_to_remove) > 0:
            for i, employee in enumerate(employees_to_remove):
                print(f"{i+1}. {employee}")
            
            choice = int(input("Enter the number of the employee to remove: "))
            
            if choice >= 1 and choice <= len(employees_to_remove):
                employee_container.remove_employee(employees_to_remove[choice-1])
                print("Employee removed successfully!")
            else:
                print("Invalid choice!")
        else:
            print("No employees found with the specified last name.")
    
    elif choice == "3":
        last_name = input("Enter last name to search: ")
        employees = employee_container.search_by_lastname(last_name)
        
        if len(employees) > 0:
            for employee in employees:
                print(employee)
        else:
            print("No employees found with the specified last name.")
    
    elif choice == "4":
        position = input("Enter position to search: ")
        employees = employee_container.search_by_position(position)
        
        if len(employees) > 0:
            for employee in employees:
                print(employee)
        else:
            print("No employees found with the specified position.")
    
    elif choice == "5":
        total_salary = employee_container.calculate_total_salary()
        print(f"Total Salary: {total_salary}")
    
    elif choice == "6":
        highest_salary_employee = employee_container.get_highest_salary_employee()
        print(f"Highest Salary Employee: {highest_salary_employee}")
    
    elif choice == "7":
        lowest_salary_employee = employee_container.get_lowest_salary_employee()
        print(f"Lowest Salary Employee: {lowest_salary_employee}")
    
    elif choice == "8":
        filename = input("Enter filename to save employees: ")
        employee_container.save_employees(filename)
        print("Employees saved successfully!")
    
    elif choice == "9":
        filename = input("Enter filename to load employees: ")
        employee_container.load_employees(filename)
        print("Employees loaded successfully!")
    
    elif choice == "0":
        break
    
    else:
        print("Invalid choice!")
