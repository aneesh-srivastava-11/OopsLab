# A program to find the second largest number in a list without using built-in sorting.

input_str = input("Enter numbers separated by space:")
nums = []
for val in input_str.strip().split():
    nums.append(int(val))
if len(set(nums)) < 2:
    print("The list does not have a second largest number.")
else:
    first = nums[0]
    for num in nums:
        if num > first:
            first = num

    second = None

    for num in nums:
        if num != first:
            if second is None or num > second:
                second = num

    print("Second largest number is:", second)