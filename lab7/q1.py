#linear search and binarySearch
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [10, 23, 45, 70, 11, 15]
key = int(input("Enter element to search: "))
print("Array:", arr)
pos = linear_search(arr, key)
if pos != -1:
    print(f"Linear Search: Element found at index {pos}")
else:
    print("Linear Search: Element not found")
sorted_arr = sorted(arr)
pos = binary_search(sorted_arr, key)
if pos != -1:
    print(f"Binary Search: Element found at index {pos} in {sorted_arr}")
else:
    print("Binary Search: Element not found")
