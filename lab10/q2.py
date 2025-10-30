try:
    # Risky code: getting input and performing division
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except ValueError:
    # Handles non-numerical input
    print("Entered value is wrong")
except ZeroDivisionError:
    # Handles division by zero
    print("Can't divide by zero")

# Example Output 1 (Input: Ten, 1):
# Enter value of a:Ten
# Entered value is wrong

# Example Output 2 (Input: 10, 0):
# Enter value of a: 10
# Enter value of b:0
# Can't divide by zero

# Example Output 3 (Input: 10, 2):
# Enter value of a: 10
# Enter value of b:2
# The answer of a divide by b: 5.0