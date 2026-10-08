## Assignment4

import numpy as np

# Enter size of matrix
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Create empty matrices
A = np.zeros((rows, columns), dtype=int)
B = np.zeros((rows, columns), dtype=int)

# Enter elements of first matrix
print("\nEnter elements of first matrix:")
for i in range(rows):
    for j in range(columns):
        A[i][j] = int(input("Enter element: "))

# Enter elements of second matrix
print("\nEnter elements of second matrix:")
for i in range(rows):
    for j in range(columns):
        B[i][j] = int(input("Enter element: ")) 

# Add the two matrices
C = np.add(A, B)
