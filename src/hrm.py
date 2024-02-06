 # src/hrm.py
from .employee import Employee

class HRM:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, role):
        if emp_id not in self.employees:
            new_employee = Employee(emp_id, name, role)
            self.employees[emp_id] = new_employee
            print(f"Employee {name} added successfully!")
        else:
            print(f"Employee ID {emp_id} already exists!")

    def get_employee(self, emp_id):
        return self.employees.get(emp_id, None)

    def list_employees(self):
        for emp_id, emp in self.employees.items():
            print(f"ID: {emp_id}, Name: {emp.name}, Role: {emp.role}, Leaves Taken: {emp.leaves_taken} days")

