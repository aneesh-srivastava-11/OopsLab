# Selection Sort in Python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]


# ---------- Main Program ----------
arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)

selection_sort(arr)
print("Sorted Array (Selection Sort):", arr)
