rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of first matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input()))
    A.append(row)

print("Enter elements of second matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input()))
    B.append(row)

C = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Addition of two matrices:")
for row in C:
    print(row)
