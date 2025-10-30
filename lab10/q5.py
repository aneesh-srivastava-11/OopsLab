try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("a/b=%d" % c)
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    # Executes only if no exception occurred in the try block
    print("We are in else block ")

# Example Output 1 (No exception, Input: 20, 4):
# Enter value of a: 20
# Enter value of b:4
# a/b=5
# We are in else block

# Example Output 2 (Exception occurred, Input: 20, 0):
# Enter value of a: 20
# Enter value of b:0
# Can't divide by zero