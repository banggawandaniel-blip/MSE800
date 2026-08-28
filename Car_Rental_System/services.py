from database import DatabaseManager
from models import Customer, Admin


class UserService:
    """Handles user registration and login."""

    def __init__(self):
        self.database = DatabaseManager()

    def register_user(self, username, password, role="customer"):
        """Register a new customer or admin."""

        cursor = self.database.connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (username, password, role)
                VALUES (?, ?, ?)
                """,
                (username, password, role)
            )

            self.database.connection.commit()

            return True, "Registration successful!"

        except Exception:
            return False, "Username already exists."

    def login_user(self, username, password):
        """Check username and password and return the user."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            SELECT id, username, password, role
            FROM users
            WHERE username = ? AND password = ?
            """,
            (username, password)
        )

        user_data = cursor.fetchone()

        if user_data is None:
            return None

        user_id, username, password, role = user_data

        if role == "customer":
            return Customer(
                user_id,
                username,
                password
            )

        if role == "admin":
            return Admin(
                user_id,
                username,
                password
            )

        return None

    def close(self):
        """Close the database connection."""

        self.database.close()


class CarService:
    """Handles car-related database operations."""

    def __init__(self):
        self.database = DatabaseManager()

    def get_all_cars(self):
        """Return all cars."""

        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT
                id,
                make,
                model,
                year,
                mileage,
                available,
                min_rent_period,
                max_rent_period,
                daily_rate
            FROM cars
        """)

        return cursor.fetchall()

    def get_available_cars(self):
        """Return only available cars."""

        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT
                id,
                make,
                model,
                year,
                mileage,
                available,
                min_rent_period,
                max_rent_period,
                daily_rate
            FROM cars
            WHERE available = 1
        """)

        return cursor.fetchall()

    def add_car(
        self,
        make,
        model,
        year,
        mileage,
        min_rent_period,
        max_rent_period,
        daily_rate
    ):
        """Add a new car."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            INSERT INTO cars (
                make,
                model,
                year,
                mileage,
                available,
                min_rent_period,
                max_rent_period,
                daily_rate
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                make,
                model,
                year,
                mileage,
                1,
                min_rent_period,
                max_rent_period,
                daily_rate
            )
        )

        self.database.connection.commit()

    def update_car(
        self,
        car_id,
        make,
        model,
        year,
        mileage,
        min_rent_period,
        max_rent_period,
        daily_rate
    ):
        """Update an existing car."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            UPDATE cars
            SET
                make = ?,
                model = ?,
                year = ?,
                mileage = ?,
                min_rent_period = ?,
                max_rent_period = ?,
                daily_rate = ?
            WHERE id = ?
            """,
            (
                make,
                model,
                year,
                mileage,
                min_rent_period,
                max_rent_period,
                daily_rate,
                car_id
            )
        )

        self.database.connection.commit()

    def delete_car(self, car_id):
        """Delete a car."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            DELETE FROM cars
            WHERE id = ?
            """,
            (car_id,)
        )

        self.database.connection.commit()

    def close(self):
        """Close the database connection."""

        self.database.close()


class BookingService:
    """Handles rental booking operations."""

    def __init__(self):
        self.database = DatabaseManager()

    def create_booking(
        self,
        customer_id,
        car_id,
        start_date,
        end_date,
        total_fee
    ):
        """Create a new rental booking."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            INSERT INTO bookings (
                customer_id,
                car_id,
                start_date,
                end_date,
                total_fee,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                customer_id,
                car_id,
                start_date,
                end_date,
                total_fee,
                "Pending"
            )
        )

        self.database.connection.commit()

    def get_customer_bookings(self, customer_id):
        """Return bookings belonging to one customer."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            SELECT
                bookings.id,
                cars.make,
                cars.model,
                bookings.start_date,
                bookings.end_date,
                bookings.total_fee,
                bookings.status
            FROM bookings
            JOIN cars
                ON bookings.car_id = cars.id
            WHERE bookings.customer_id = ?
            """,
            (customer_id,)
        )

        return cursor.fetchall()

    def get_all_bookings(self):
        """Return all bookings for the admin."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            SELECT
                bookings.id,
                users.username,
                cars.make,
                cars.model,
                bookings.start_date,
                bookings.end_date,
                bookings.total_fee,
                bookings.status
            FROM bookings
            JOIN users
                ON bookings.customer_id = users.id
            JOIN cars
                ON bookings.car_id = cars.id
            ORDER BY bookings.id DESC
            """
        )

        return cursor.fetchall()

    def update_booking_status(
        self,
        booking_id,
        status
    ):
        """Approve or reject a booking."""

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            UPDATE bookings
            SET status = ?
            WHERE id = ?
            """,
            (
                status,
                booking_id
            )
        )

        self.database.connection.commit()

    def close(self):
        """Close the database connection."""

        self.database.close()