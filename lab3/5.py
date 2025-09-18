# Program to find the sum of digits of a number until the sum becomes a single digit.

num = int(input("Enter a number:"))
sum_val = 0
while num > 0:
    sum_val += num % 10
    num = num // 10

while sum_val >= 10:
    temp_sum = 0
    while sum_val > 0:
        temp_sum += sum_val % 10
        sum_val //= 10
    sum_val = temp_sum

print(f"The final single-digit sum is: {sum_val}")