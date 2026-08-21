Money Exchange System
Project Overview
The Money Exchange System is a database application designed to help a currency exchange business manage customers, currencies, exchange rates, and currency exchange transactions. The system uses Python with an object-oriented programming (OOP) approach and an SQLite database.
Project Scope
The system allows the exchange business to:
•	Manage customer information.
•	Manage supported currencies.
•	Store exchange rates between currencies.
•	Record currency exchange transactions.
•	Calculate and store the converted amount for each transaction.
Database Tables
The database contains 4 tables:
1. Customer
The Customer table stores information about customers who use the money exchange service.
Attributes:
•	customer_id - Primary key that uniquely identifies each customer.
•	first_name - Customer's first name.
•	last_name - Customer's last name.
•	email - Customer's email address.
•	phone - Customer's phone number.
This table is necessary because the business needs to identify and manage customers who perform currency exchange transactions.
2. Currency
The Currency table stores the currencies supported by the money exchange system.
Attributes:
•	currency_id - Primary key that uniquely identifies each currency.
•	currency_code - Three-letter currency code such as NZD, USD, PHP, or AUD.
•	currency_name - Full name of the currency.
•	symbol - Currency symbol.
This table is necessary because the exchange business needs to maintain a list of currencies that can be exchanged.
3. ExchangeRate
The ExchangeRate table stores the exchange rate between two currencies.
Attributes:
•	rate_id - Primary key that uniquely identifies each exchange rate.
•	from_currency_id - Foreign key identifying the currency being exchanged.
•	to_currency_id - Foreign key identifying the currency being received.
•	rate - Exchange rate used for the conversion.
•	effective_date - Date when the exchange rate applies.
This table is necessary because exchange rates can change over time and the business needs to store the rates used for currency conversions.
4. ExchangeTransaction
The ExchangeTransaction table records the actual currency exchanges made by customers.
Attributes:
•	transaction_id - Primary key that uniquely identifies each transaction.
•	customer_id - Foreign key identifying the customer.
•	rate_id - Foreign key identifying the exchange rate used.
•	from_currency_id - Foreign key identifying the source currency.
•	to_currency_id - Foreign key identifying the target currency.
•	amount - Amount of money exchanged.
•	converted_amount - Amount received after conversion.
•	transaction_date - Date of the transaction.
This table is necessary because the business needs to keep a record of every currency exchange transaction.
Entity Relationships
The main relationships in the database are:
•	One customer can make many exchange transactions.
•	One exchange rate can be used for many exchange transactions.
•	One currency can be used in many exchange rate records.
•	One currency can be used in many exchange transactions as either the source or target currency.
Object-Oriented Programming
The project uses Python classes to represent the main entities in the system.
The following classes are implemented in models.py:
•	Customer
•	Currency
•	ExchangeRate
•	ExchangeTransaction
These classes use objects to represent data and demonstrate the use of object-oriented programming principles.
Sample Data
The database includes sample data for:
•	2 customers
•	4 currencies
•	3 exchange rates
•	2 exchange transactions
The currencies used in the sample data are:
•	NZD - New Zealand Dollar
•	USD - United States Dollar
•	PHP - Philippine Peso
•	AUD - Australian Dollar
Technologies Used
•	Python
•	SQLite
•	Object-Oriented Programming (OOP)
•	Visual Studio Code
•	GitHub
•	Draw.io / diagrams.net
How to Run the Project
1.	Open the project folder in Visual Studio Code.
2.	Make sure Python is installed.
3.	Open the VS Code terminal.
4.	Run the database creation program:
python database.py
5.	Run the main program:
python main.py
The program will create the database tables and populate them with sample data.
Project Files
money_exchange_system/
│
├── database.py
├── main.py
├── models.py
├── money_exchange.db
└── README.md
Conclusion
The Money Exchange System provides a simple database solution for managing customers, currencies, exchange rates, and currency exchange transactions. The database structure uses primary keys and foreign keys to maintain relationships between the tables, while Python classes demonstrate the use of object-oriented programming.
