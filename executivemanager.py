# Author: Amonn Burns
# Date: 2/18/26
# File:executivemanager.py
# Description: Define ExecutiveManager class
from manager import Manager
from person import Person

class ExecutiveManager(Manager):
    def __init__(self, person: Person, emp_id: int, years_of_service: int, salary: int, department: str, bonus: int):
        super().__init__(person, emp_id, years_of_service, salary, department)
        self.bonus = bonus

    def calculate_payment(self) -> float:
        return self.salary + self.bonus

    def to_dict(self) -> dict:
        base = super().to_dict()
        base['Payment Amount'] = self.calculate_payment()
        base['Department'] = self.department
        base['Salary'] = self.salary
        base['Bonus'] = self.bonus
        return base
