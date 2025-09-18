# Program to print all prime numbers below 100.

print("Prime numbers below 100:")
for num in range(2, 100):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)