# Author: Amonn Burns
# Date: 2/18/26
# File:secretary.py
# Description: Define Secretary Class
from payroll.models import Employee
from person import Person


class Secretary(Employee):
    def __init__(self, person: Person, emp_id: int, years_of_service: int, wage: float, hours: int):
        super().__init__(person, emp_id, years_of_service)
        self.wage = wage
        self.hours = hours

    def calculate_payment(self) -> float:
        return self.wage * self.hours

    def to_dict(self) -> dict:
        base = super().to_dict()
        base['Payment Amount'] = self.calculate_payment()
        base['Wage'] = self.wage
        base['Hours'] = self.hours
        return base