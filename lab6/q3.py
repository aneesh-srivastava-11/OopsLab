a = int(input("Enter starting point of range: "))
b = int(input("Enter end point of range: "))

def is_armstrong(n):
    power = len(str(n))  # Number of digits
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == n

print(f"Armstrong numbers between {a} and {b}:")
for num in range(a, b + 1):
    if is_armstrong(num):
        print(num)