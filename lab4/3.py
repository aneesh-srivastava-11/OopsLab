# Program to remove duplicates from a list.

input_str = input("Enter numbers separated by space:")
nums = [int(val) for val in input_str.strip().split()]

unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)