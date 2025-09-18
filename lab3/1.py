# Program to generate Fibonacci sequence.

n = int(input("Enter number of fibonacci terms needed:"))
if n < 0:
    print("Please enter a positive number.")
elif n == 0:
    print("0")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b