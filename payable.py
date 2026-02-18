# Author: Amonn Burns
# Date: 2/18/26
# File:models.py
# Description: Define the Payable class
from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def calculate_payment(self) -> float:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass