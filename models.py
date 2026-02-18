# Author: Amonn Burns
# Date: 2/18/26
# File:models.py
# Description: Define the Payable class
from payable import Payable
from person import Person

class Employee(Payable):
    employee_count=0
    def __init__(self, person: Person, emp_id: int, years_of_service: int):
        self.person = person
        self.employee_id = emp_id
        self.years_of_service = years_of_service
        Employee.employee_count+=1

    def calculate_payment(self) -> float:
        pass

    def to_dict(self):
        result = {"Employee ID": self.employee_id
        }
        result.update(self.person.to_dict())
        result["Years of Service"] = self.years_of_service
        return result

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count