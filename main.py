from functions import Calculator
from utils import enter_hours

hours = enter_hours()

calc1 = Calculator(hours)

payment = calc1.payment_total()

print(f"The total salay of this month so far is: {payment:,.0f} COP".replace(",", "."))