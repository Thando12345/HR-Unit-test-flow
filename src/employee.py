 # src/employee.py

class Employee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.leaves_taken = 0

    def request_leave(self, days):
        self.leaves_taken += days
        print(f"{self.name} has taken {days} days off. Total leaves taken: {self.leaves_taken} days.")

