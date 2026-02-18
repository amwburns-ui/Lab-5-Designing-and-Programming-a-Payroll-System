# Author: Amonn Burns
# Date: 2/18/26
# File:salesperson.py
# Description: Define Salesperson Class
from payroll.models import Employee
from person import Person


class Salesperson(Employee):
    def __init__(self, person: Person, emp_id: int, years_of_service: int, sales: float, commission_rate: float):
        super().__init__(person, emp_id, years_of_service)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_payment(self) -> float:
        return self.sales * self.commission_rate

    def to_dict(self) -> dict:
        base = super().to_dict()
        base['Payment Amount'] = self.calculate_payment()
        base['Sales'] = self.sales
        base['Commission Rate'] = self.commission_rate
        return base
