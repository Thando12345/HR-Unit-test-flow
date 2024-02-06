# tests/test_hrm.py
import unittest
from src.hrm import HRM

class TestHRM(unittest.TestCase):

    def setUp(self):
        # Create an instance of HRM for testing
        self.hrm_system = HRM()

    def tearDown(self):
        # Clean up after each test if necessary
        pass

    def test_add_employee(self):
        # Test adding an employee
        self.hrm_system.add_employee(1, "John Doe", "Software Engineer")
        employee = self.hrm_system.get_employee(1)
        
        # Assert that the employee was added successfully
        self.assertIsNotNone(employee)
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.role, "Software Engineer")

    def test_add_existing_employee(self):
        # Test adding an employee with an existing ID
        self.hrm_system.add_employee(1, "John Doe", "Software Engineer")
        
        # Attempt to add the same employee again
        self.hrm_system.add_employee(1, "Jane Smith", "Data Scientist")

        # Assert that the second attempt fails
        self.assertEqual(len(self.hrm_system.employees), 1)

    def test_get_nonexistent_employee(self):
        # Test getting a non-existent employee
        employee = self.hrm_system.get_employee(100)

        # Assert that the employee is None
        self.assertIsNone(employee)

    def test_list_employees(self):
        # Test listing employees
        self.hrm_system.add_employee(1, "John Doe", "Software Engineer")
        self.hrm_system.add_employee(2, "Jane Smith", "Data Scientist")
        
        # Redirect standard output for testing
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Call the list_employees method
        self.hrm_system.list_employees()

        # Get the printed output
        printed_output = sys.stdout.getvalue()

        # Reset standard output
        sys.stdout = original_stdout

        # Assert that the output contains expected information
        self.assertIn("John Doe", printed_output)
        self.assertIn("Jane Smith", printed_output)
        self.assertIn("Software Engineer", printed_output)
        self.assertIn("Data Scientist", printed_output)

if __name__ == "__main__":
    unittest.main()
