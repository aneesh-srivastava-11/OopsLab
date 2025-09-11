def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def is_strong_number(num):
    original = num
    total = 0
    while num > 0:
        digit = num % 10
        total += factorial(digit)
        num //= 10
    return total == original
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number ")
else:
    print(f"{number} is NOT a Strong Number.")