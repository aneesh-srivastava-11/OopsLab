try:
    # Risky code
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except (ValueError, ZeroDivisionError):
    # Handles either ValueError (e.g., non-numeric input) or ZeroDivisionError
    print("Please enter a valid value")
