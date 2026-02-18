# Author: Amonn Burns
# Date: 2/18/26
# File:person.py
# Description: Define Person class

class Person:
    def __init__(self, first_name: str, last_name: str, gender: str, ssn: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.ssn = ssn

    def to_dict(self) -> dict:
        return {
            'Name': f"{self.first_name} {self.last_name}",
            'Gender': self.gender,
            'Social Security Number': self.ssn,
        }