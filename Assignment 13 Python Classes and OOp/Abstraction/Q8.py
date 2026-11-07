# Q8 - Payment Gateway (Abstraction)

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def _validate_amount(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        return amount


class CardPayment(PaymentMethod):
    def pay(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Card | Transaction: Payment | Amount: Rs. {amount:,.2f}")

    def refund(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Card | Transaction: Refund | Amount: Rs. {amount:,.2f}")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Wallet | Transaction: Payment | Amount: Rs. {amount:,.2f}")

    def refund(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Wallet | Transaction: Refund | Amount: Rs. {amount:,.2f}")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Bank Transfer | Transaction: Payment | Amount: Rs. {amount:,.2f}")

    def refund(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Bank Transfer | Transaction: Refund | Amount: Rs. {amount:,.2f}")


# Extension: a new payment method can be added without changing this dispatcher.
class MobileWalletPayment(PaymentMethod):
    def pay(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Mobile Wallet | Transaction: Payment | Amount: Rs. {amount:,.2f}")

    def refund(self, amount):
        self._validate_amount(amount)
        print(f"Payment method: Mobile Wallet | Transaction: Refund | Amount: Rs. {amount:,.2f}")


def process_transaction(method, transaction_type, amount):
    if transaction_type == "pay":
        method.pay(amount)
    elif transaction_type == "refund":
        method.refund(amount)
    else:
        raise ValueError("Transaction type must be 'pay' or 'refund'.")


if __name__ == "__main__":
    payment_methods = [
        CardPayment(),
        WalletPayment(),
        BankTransferPayment(),
        MobileWalletPayment()
    ]

    for payment_method in payment_methods:
        process_transaction(payment_method, "pay", 2500)
        process_transaction(payment_method, "refund", 500)

    try:
        process_transaction(CardPayment(), "pay", -100)
    except ValueError as error:
        print(f"Transaction rejected: {error}")
