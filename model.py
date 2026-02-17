import sqlite3
from datetime import datetime

class CalculatorModel:
    def __init__(self):
        self.currency_data = { "Colombia": "COP",
            "United States": "USD",
            "Canada": "CAD",
            "European Union": "EUR",
            "United Kingdom": "GBP",
            "Mexico": "MXN",
            "Japan": "JPY",
            "Australia": "AUD" }
        
        self.init_db()

    def init_db(self):
        self.conn = sqlite3.connect('salary_history.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                country TEXT,
                hours REAL,
                rate REAL,
                total REAL
            )
        ''')
        self.conn.commit()

    def save_calculation(self, country, hours, rate, total):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO calculations (date, country, hours, rate, total)
            VALUES (?, ?, ?, ?, ?)
        ''', (date_now, country, hours, rate, total))
        self.conn.commit()

    def get_last_calculation(self):
        self.cursor.execute('SELECT * FROM calculations ORDER BY id DESC LIMIT 1')
        return self.cursor.fetchone()
    def calculate_payment(self, hours, rate):
        return hours * rate

    def get_currency_code(self, country):
        return self.currency_data.get(country, "USD")

    def get_country_list(self):
        return sorted(self.currency_data.keys())