# Program to represent a 2D list as a matrix and perform addition, subtraction, and transpose.

rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

A = []
print("Enter matrix A:")
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

B = []
print("Enter matrix B:")
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

# Initialize result matrices
add = []
sub = []

# Addition and subtraction
for i in range(rows):
    add_row = []
    sub_row = []
    for j in range(cols):
        add_row.append(A[i][j] + B[i][j])
        sub_row.append(A[i][j] - B[i][j])
    add.append(add_row)
    sub.append(sub_row)

# Transpose
transpose = []
for j in range(cols):
    t_row = []
    for i in range(rows):
        t_row.append(A[i][j])
    transpose.append(t_row)

# Print results
print("Addition:", add)
print("Subtraction:", sub)
print("Transpose of A:", transpose)