class User:
    """Base class for all system users."""

    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def display_info(self):
        """Display basic user information."""
        return f"Username: {self.username}, Role: {self.role}"


class Customer(User):
    """Represents a customer who can rent cars."""

    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, "customer")


class Admin(User):
    """Represents an administrator who manages the system."""

    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, "admin")


class Car:
    """Represents a car available for rental."""

    def __init__(
        self,
        car_id,
        make,
        model,
        year,
        mileage,
        available,
        min_rent_period,
        max_rent_period,
        daily_rate
    ):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period
        self.daily_rate = daily_rate

    def display_info(self):
        """Return the car's details."""
        availability = "Available" if self.available else "Not Available"

        return (
            f"{self.make} {self.model} ({self.year})\n"
            f"Mileage: {self.mileage} km\n"
            f"Daily Rate: ${self.daily_rate:.2f}\n"
            f"Rental Period: {self.min_rent_period}-"
            f"{self.max_rent_period} days\n"
            f"Status: {availability}"
        )


class Booking:
    """Represents a customer's car rental booking."""

    def __init__(
        self,
        booking_id,
        customer_id,
        car_id,
        start_date,
        end_date,
        total_fee,
        status="Pending"
    ):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_fee = total_fee
        self.status = status

    def approve(self):
        """Approve the booking."""
        self.status = "Approved"

    def reject(self):
        """Reject the booking."""
        self.status = "Rejected"

    def display_info(self):
        """Return booking information."""
        return (
            f"Booking ID: {self.booking_id}\n"
            f"Customer ID: {self.customer_id}\n"
            f"Car ID: {self.car_id}\n"
            f"Start Date: {self.start_date}\n"
            f"End Date: {self.end_date}\n"
            f"Total Fee: ${self.total_fee:.2f}\n"
            f"Status: {self.status}"
        )