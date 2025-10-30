try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except ZeroDivisionError as e:
    # Catch the ZeroDivisionError and raise a new ValueError,
    # linking them with 'from e'
    raise ValueError("Division failed") from e

# Example execution (Input: 10, 0):
# Enter value of a:10
# Enter value of b:0
# Traceback (most recent call last):
#   ... (traceback for ZeroDivisionError)
# ZeroDivisionError: division by zero
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   ... (traceback for ValueError)
# ValueError: Division failed