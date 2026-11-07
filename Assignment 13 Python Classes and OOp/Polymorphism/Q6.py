# Q6 - Checkout Discount Calculator (Polymorphism)

class RegularCustomer:
    discount_rate = 0.05

    def final_price(self, amount):
        return calculate_discounted_price(amount, self.discount_rate)


class PremiumCustomer:
    discount_rate = 0.10

    def final_price(self, amount):
        return calculate_discounted_price(amount, self.discount_rate)


class VIPCustomer:
    discount_rate = 0.20

    def final_price(self, amount):
        return calculate_discounted_price(amount, self.discount_rate)


class GoldCustomer:
    discount_rate = 0.15

    def final_price(self, amount):
        return calculate_discounted_price(amount, self.discount_rate)


def calculate_discounted_price(amount, discount_rate):
    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Bill amount cannot be negative and must be numeric.")
    return amount * (1 - discount_rate)


def print_receipt(customer, amount):
    final_amount = customer.final_price(amount)
    print(f"{customer.__class__.__name__}: Rs. {final_amount:,.2f}")


if __name__ == "__main__":
    customers = [
        RegularCustomer(),
        PremiumCustomer(),
        VIPCustomer(),
        GoldCustomer()
    ]

    for customer in customers:
        print_receipt(customer, 10000)

    try:
        print_receipt(RegularCustomer(), -500)
    except ValueError as error:
        print(f"Invalid bill: {error}")

    # GoldCustomer is added without changing print_receipt().
