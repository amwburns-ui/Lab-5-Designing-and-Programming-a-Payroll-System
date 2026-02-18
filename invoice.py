# Author: Amonn Burns
# Date: 2/18/26
# File:invoice.py
# Description: Define the Invoice class
from payable import Payable

class Invoice(Payable):
    invoice_count_integer=0
    def __init__(self, part_name: str, price: float, quantity: int):
        self.part_name = part_name
        self.price = price
        self.quantity = quantity
        Invoice.invoice_count_integer+=1

    def calculate_payment(self) -> float:
        return self.price * self.quantity

    def to_dict(self) -> dict:
        return {'part_name': self.part_name, 'price': self.price, 'quantity': self.quantity}

    @classmethod
    def get_invoice_count(cls) -> int:
        return Invoice.invoice_count_integer