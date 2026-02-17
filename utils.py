def enter_hours():
    while True:
        try:
            hours = float(input("Enter the hours you worked this month: "))
            return hours
        except ValueError:
            print("Please enter a valid number.")
            
