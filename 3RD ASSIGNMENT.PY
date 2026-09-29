from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, payment_amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self, payment_amount):
        print(f"Paid ₹{payment_amount} using Credit Card.")


class UPIPayment(PaymentStrategy):

    def pay(self, payment_amount):
        print(f"Paid ₹{payment_amount} using UPI.")


class PayPalPayment(PaymentStrategy):

    def pay(self, payment_amount):
        print(f"Paid ₹{payment_amount} using PayPal.")


class PaymentProcessor:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def set_strategy(self, new_method):
        self.payment_method = new_method

    def process_payment(self, payment_amount):
        self.payment_method.pay(payment_amount)


payment_system = PaymentProcessor(CreditCardPayment())

print("Payment Method: Credit Card")
payment_system.process_payment(2500)

print("\nChanging Payment Method to UPI")
payment_system.set_strategy(UPIPayment())
payment_system.process_payment(1800)

print("\nChanging Payment Method to PayPal")
payment_system.set_strategy(PayPalPayment())
payment_system.process_payment(3200)