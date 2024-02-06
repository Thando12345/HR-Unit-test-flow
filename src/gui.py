# src/gui.py
import tkinter as tk
from tkinter import scrolledtext
from src.hrm import HRM, Employee  # Update the import statements

class HRMGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("HRM System")

        # Initialize HRM system with mock data
        self.hrm_system = HRM()
        self.hrm_system.add_employee(1, "John Doe", "Software Engineer")
        self.hrm_system.add_employee(2, "Jane Smith", "Data Scientist")

        # Styling
        self.master.configure(bg='#E5E5E5')  # Set background color

        self.label = tk.Label(master, text="HRM System", font=("Helvetica", 16), bg='#4CAF50', fg='white')
        self.label.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Employee", command=self.add_employee, bg='#4CAF50', fg='white')
        self.add_button.pack(pady=5)

        self.get_button = tk.Button(master, text="Get Employee", command=self.get_employee, bg='#2196F3', fg='white')
        self.get_button.pack(pady=5)

        self.list_button = tk.Button(master, text="List Employees", command=self.list_employees, bg='#FF9800', fg='white')
        self.list_button.pack(pady=5)

    def add_employee(self):
        # Create a new window for input
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Employee")

        # Styling
        add_window.configure(bg='#E5E5E5')  # Set background color

        emp_id_label = tk.Label(add_window, text="Employee ID:", bg='#E5E5E5')
        emp_id_label.pack()
        emp_id_entry = tk.Entry(add_window)
        emp_id_entry.pack()

        name_label = tk.Label(add_window, text="Name:", bg='#E5E5E5')
        name_label.pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        role_label = tk.Label(add_window, text="Role:", bg='#E5E5E5')
        role_label.pack()
        role_entry = tk.Entry(add_window)
        role_entry.pack()

        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.submit_employee(
            emp_id_entry.get(), name_entry.get(), role_entry.get(), add_window), bg='#4CAF50', fg='white')
        submit_button.pack(pady=5)

    def submit_employee(self, emp_id, name, role, window):
        try:
            emp_id = int(emp_id)
        except ValueError:
            print("Invalid Employee ID. Please enter a valid integer.")
            return

        self.hrm_system.add_employee(emp_id, name, role)
        window.destroy()

    def get_employee(self):
        # Create a new window for input
        get_window = tk.Toplevel(self.master)
        get_window.title("Get Employee")

        # Styling
        get_window.configure(bg='#E5E5E5')  # Set background color

        emp_id_label = tk.Label(get_window, text="Employee ID:", bg='#E5E5E5')
        emp_id_label.pack()
        emp_id_entry = tk.Entry(get_window)
        emp_id_entry.pack()

        submit_button = tk.Button(get_window, text="Submit", command=lambda: self.display_employee(
            emp_id_entry.get(), get_window), bg='#2196F3', fg='white')
        submit_button.pack(pady=5)

    # Rest of the code remains unchanged

    def list_employees(self):
        # Create a new window for displaying employees
        list_window = tk.Toplevel(self.master)
        list_window.title("List Employees")

        # Styling
        list_window.configure(bg='#E5E5E5')  # Set background color

        # Use scrolledtext for displaying the list
        result_text = scrolledtext.ScrolledText(list_window, width=40, height=10, bg='#FFFFFF', fg='#333333')
        result_text.pack()

        # Get the list of employees from the HRM system and format it for display
        employees_list = self.hrm_system.list_employees()

        if employees_list:
            formatted_list = "\n".join([f"ID: {emp.emp_id}, Name: {emp.name}, Role: {emp.role}" for emp in employees_list])
            result_text.insert(tk.END, formatted_list)
        else:
            result_text.insert(tk.END, "No employees found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HRMGUI(root)
    root.mainloop()
