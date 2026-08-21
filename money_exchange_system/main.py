import sqlite3
from pathlib import Path

from models import Customer, Currency, ExchangeRate, ExchangeTransaction


def add_sample_data():
    # Connect to the database
    db_path = Path(__file__).resolve().parent / "money_exchange.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # -------------------------
    # CUSTOMERS
    # -------------------------

    customer1 = Customer(
        "John",
        "Smith",
        "john@example.com",
        "0211234567"
    )

    customer2 = Customer(
        "Maria",
        "Santos",
        "maria@example.com",
        "0227654321"
    )

    cursor.execute("""
        INSERT INTO Customer (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
    """, (
        customer1.first_name,
        customer1.last_name,
        customer1.email,
        customer1.phone
    ))

    cursor.execute("""
        INSERT INTO Customer (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
    """, (
        customer2.first_name,
        customer2.last_name,
        customer2.email,
        customer2.phone
    ))

    # -------------------------
    # CURRENCIES
    # -------------------------

    currencies = [
        Currency("NZD", "New Zealand Dollar", "$"),
        Currency("USD", "United States Dollar", "$"),
        Currency("PHP", "Philippine Peso", "₱"),
        Currency("AUD", "Australian Dollar", "$")
    ]

    for currency in currencies:
        cursor.execute("""
            INSERT OR IGNORE INTO Currency
            (currency_code, currency_name, symbol)
            VALUES (?, ?, ?)
        """, (
            currency.currency_code,
            currency.currency_name,
            currency.symbol
        ))

    # Get currency IDs
    cursor.execute("SELECT currency_id, currency_code FROM Currency")
    currency_data = cursor.fetchall()

    currency_ids = {
        code: currency_id
        for currency_id, code in currency_data
    }

    # -------------------------
    # EXCHANGE RATES
    # -------------------------

    rate1 = ExchangeRate(
        currency_ids["NZD"],
        currency_ids["USD"],
        0.60,
        "2026-08-21"
    )

    rate2 = ExchangeRate(
        currency_ids["NZD"],
        currency_ids["PHP"],
        34.50,
        "2026-08-21"
    )

    rate3 = ExchangeRate(
        currency_ids["NZD"],
        currency_ids["AUD"],
        0.91,
        "2026-08-21"
    )

    rates = [rate1, rate2, rate3]

    for rate in rates:
        cursor.execute("""
            INSERT INTO ExchangeRate
            (from_currency_id, to_currency_id, rate, effective_date)
            VALUES (?, ?, ?, ?)
        """, (
            rate.from_currency_id,
            rate.to_currency_id,
            rate.rate,
            rate.effective_date
        ))

    # Get exchange rate IDs
    cursor.execute("""
        SELECT rate_id, from_currency_id, to_currency_id
        FROM ExchangeRate
    """)

    rate_data = cursor.fetchall()

    rate_ids = {}

    for rate_id, from_id, to_id in rate_data:
        rate_ids[(from_id, to_id)] = rate_id

    # -------------------------
    # EXCHANGE TRANSACTIONS
    # -------------------------

    transaction1 = ExchangeTransaction(
        1,
        rate_ids[
            (currency_ids["NZD"], currency_ids["PHP"])
        ],
        currency_ids["NZD"],
        currency_ids["PHP"],
        100,
        3450,
        "2026-08-21"
    )

    transaction2 = ExchangeTransaction(
        2,
        rate_ids[
            (currency_ids["NZD"], currency_ids["USD"])
        ],
        currency_ids["NZD"],
        currency_ids["USD"],
        200,
        120,
        "2026-08-21"
    )

    transactions = [transaction1, transaction2]

    for transaction in transactions:
        cursor.execute("""
            INSERT INTO ExchangeTransaction
            (
                customer_id,
                rate_id,
                from_currency_id,
                to_currency_id,
                amount,
                converted_amount,
                transaction_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction.customer_id,
            transaction.rate_id,
            transaction.from_currency_id,
            transaction.to_currency_id,
            transaction.amount,
            transaction.converted_amount,
            transaction.transaction_date
        ))

    connection.commit()
    connection.close()

    print("Sample data added successfully.")
    print("Exchange rates added successfully.")
    print("Exchange transactions added successfully.")


if __name__ == "__main__":
    add_sample_data()