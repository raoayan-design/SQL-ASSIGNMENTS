# Q2 - Secure Bank Account (Encapsulation)

class BankAccount:
    def __init__(self, account_holder, pin, opening_balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = 0                    # Private attribute
        self.__pin = str(pin)                 # Private attribute

        if not self.__pin.isdigit() or len(self.__pin) != 4:
            raise ValueError("PIN must contain exactly 4 digits.")
        if isinstance(opening_balance, bool) or not isinstance(opening_balance, (int, float)) or opening_balance < 0:
            raise ValueError("Opening balance must be a non-negative number.")

        self.__balance = opening_balance

    def deposit(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit rejected: amount must be positive.")
            return False
        self.__balance += amount
        print(f"Deposit successful: Rs. {amount:,.2f}")
        return True

    def withdraw(self, amount, pin):
        if str(pin) != self.__pin:
            print("Withdrawal rejected: incorrect PIN.")
            return False
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal rejected: amount must be positive.")
            return False
        if amount > self.__balance:
            print("Withdrawal rejected: insufficient balance.")
            return False

        self.__balance -= amount
        print(f"Withdrawal successful: Rs. {amount:,.2f}")
        return True

    def get_balance(self, pin):
        if str(pin) != self.__pin:
            print("Balance unavailable: incorrect PIN.")
            return None
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Subhan", "2468", 5000)

    account.deposit(1500)             # Successful deposit
    account.withdraw(1000, "2468")   # Successful withdrawal
    account.withdraw(9000, "2468")   # Rejected: insufficient balance
    account.withdraw(500, "1111")    # Rejected: incorrect PIN
    print(f"Current balance: Rs. {account.get_balance('2468'):,.2f}")
