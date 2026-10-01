# Write a Python program which takes two digits m(rows) and n(column) as input and generates a 2D array. The element value in the i-th row and j-th column of the array should be i*j
m = 3
n = 4

array = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i*j)
    array.append(row)
print(array)        
