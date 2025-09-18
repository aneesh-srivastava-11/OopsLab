# Program to rotate a list to the right/left by k positions.

input_str = input("Enter list elements:")
nums = [int(val) for val in input_str.strip().split()]
k = int(input("Enter rotation count:"))
direction = input("Rotate Left or Right (L/R):").strip().upper()
n = len(nums)
k = k % n

if direction == 'L':
    rotated = nums[k:] + nums[:k]
elif direction == 'R':
    rotated = nums[-k:] + nums[:-k]
else:
    print("Invalid direction. No rotation performed.")
    rotated = nums

print("Rotated list:", rotated)