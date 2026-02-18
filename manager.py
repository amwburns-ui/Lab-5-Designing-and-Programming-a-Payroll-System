# Author: Amonn Burns
# Date: 2/18/26
# File:manager.py
# Description: Define Manager Class
from payroll.models import Employee
from person import Person


class Manager(Employee):
    def __init__(self, person: Person, emp_id: int, years_of_service: int, salary: int, department: str):
        super().__init__(person, emp_id, years_of_service)
        self.salary = salary
        self.department = department

    def calculate_payment(self) -> float:
        return self.salary

    def to_dict(self) -> dict:
        base = super().to_dict()
        base['Payment Amount'] = self.calculate_payment()
        base['Department'] = self.department
        base['Salary'] = self.salary
        return base