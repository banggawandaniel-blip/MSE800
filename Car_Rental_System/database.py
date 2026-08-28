import sqlite3
import os


class DatabaseManager:
    """Manages the SQLite database for the car rental system."""

    def __init__(self):
        # Create the data folder if it does not already exist
        os.makedirs("data", exist_ok=True)

        # Location of our database file
        self.database_path = "data/car_rental.db"

        # Connect to the database
        self.connection = sqlite3.connect(self.database_path)

        # Create the required tables
        self.create_tables()

    def create_tables(self):
        """Create the database tables if they do not already exist."""

        cursor = self.connection.cursor()

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)

        # Cars table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                mileage INTEGER NOT NULL,
                available INTEGER NOT NULL DEFAULT 1,
                min_rent_period INTEGER NOT NULL,
                max_rent_period INTEGER NOT NULL,
                daily_rate REAL NOT NULL
            )
        """)

        # Bookings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                car_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                total_fee REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending',
                FOREIGN KEY (customer_id) REFERENCES users(id),
                FOREIGN KEY (car_id) REFERENCES cars(id)
            )
        """)

        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()


if __name__ == "__main__":
    database = DatabaseManager()
    print("Database created successfully!")
    database.close()