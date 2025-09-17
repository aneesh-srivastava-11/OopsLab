# Bubble Sort in Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# ---------- Main Program ----------
arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)

bubble_sort(arr)
print("Sorted Array (Bubble Sort):", arr)
