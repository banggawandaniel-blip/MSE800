from database import DatabaseManager


database = DatabaseManager()

cursor = database.connection.cursor()

cursor.execute("""
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
""", (
    "Toyota",
    "Corolla",
    2024,
    15000,
    1,
    1,
    30,
    60.00
))

database.connection.commit()

print("Test car added successfully!")

database.close()