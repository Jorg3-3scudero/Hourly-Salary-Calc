class Calculator:
    def __init__(self, hours):
        self.hours = hours
        self.payment = 0

    def payment_total(self):
        self.payment = self.hours * 13000
        return self.payment