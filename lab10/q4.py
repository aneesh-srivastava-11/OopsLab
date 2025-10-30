try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except ZeroDivisionError:
    print("Can't divide with zero")
finally:
    # This block always executes
    print("Inside a finally block")

# Example Output 1 (No exception, Input: 20, 5):
# Enter value of a:20
# Enter value of b:5
# The answer of a divide by b: 4.0
# Inside a finally block

# Example Output 2 (Exception caught, Input: 20, 0):
# Enter value of a:20
# Enter value of b:0
# Can't divide with zero
# Inside a finally block