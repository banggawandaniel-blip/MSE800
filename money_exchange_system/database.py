import sqlite3
from pathlib import Path


def create_database():
    # Create the database in the same folder as this Python file
    db_path = Path(__file__).resolve().parent / "money_exchange.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Customer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT
        )
    """)

    # Currency table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Currency (
            currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code TEXT NOT NULL UNIQUE,
            currency_name TEXT NOT NULL,
            symbol TEXT
        )
    """)

    # Exchange Rate table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ExchangeRate (
            rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_currency_id INTEGER NOT NULL,
            to_currency_id INTEGER NOT NULL,
            rate REAL NOT NULL,
            effective_date TEXT NOT NULL,
            FOREIGN KEY (from_currency_id) REFERENCES Currency(currency_id),
            FOREIGN KEY (to_currency_id) REFERENCES Currency(currency_id)
        )
    """)

    # Exchange Transaction table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ExchangeTransaction (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            rate_id INTEGER NOT NULL,
            from_currency_id INTEGER NOT NULL,
            to_currency_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            converted_amount REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
            FOREIGN KEY (rate_id) REFERENCES ExchangeRate(rate_id),
            FOREIGN KEY (from_currency_id) REFERENCES Currency(currency_id),
            FOREIGN KEY (to_currency_id) REFERENCES Currency(currency_id)
        )
    """)

    connection.commit()
    connection.close()

    print("Database and tables created successfully.")


if __name__ == "__main__":
    create_database()