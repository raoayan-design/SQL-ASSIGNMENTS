# Q4 - Vehicle Rental System (Inheritance)

class Vehicle:
    def __init__(self, brand, model, daily_rate):
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate

    def calculate_rent(self, days):
        if isinstance(days, bool) or not isinstance(days, int) or days <= 0:
            raise ValueError("Rental duration must be a positive whole number of days.")
        return self.daily_rate * days


class Car(Vehicle):
    INSURANCE_PER_RENTAL = 1000

    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        return base_rent + self.INSURANCE_PER_RENTAL


class Bike(Vehicle):
    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        return base_rent * 0.90  # 10% discount on base rental amount


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 5000)
    bike = Bike("Honda", "CD 70", 1500)

    print(f"Car rent for 3 days (including insurance): Rs. {car.calculate_rent(3):,.2f}")
    print(f"Bike rent for 3 days (after 10% discount): Rs. {bike.calculate_rent(3):,.2f}")

    try:
        car.calculate_rent(0)
    except ValueError as error:
        print(f"Invalid rental: {error}")
