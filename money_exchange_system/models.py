class Customer:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


class Currency:
    def __init__(self, currency_code, currency_name, symbol):
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.symbol = symbol


class ExchangeRate:
    def __init__(self, from_currency_id, to_currency_id, rate, effective_date):
        self.from_currency_id = from_currency_id
        self.to_currency_id = to_currency_id
        self.rate = rate
        self.effective_date = effective_date


class ExchangeTransaction:
    def __init__(
        self,
        customer_id,
        rate_id,
        from_currency_id,
        to_currency_id,
        amount,
        converted_amount,
        transaction_date
    ):
        self.customer_id = customer_id
        self.rate_id = rate_id
        self.from_currency_id = from_currency_id
        self.to_currency_id = to_currency_id
        self.amount = amount
        self.converted_amount = converted_amount
        self.transaction_date = transaction_date
        