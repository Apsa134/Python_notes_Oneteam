matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
rows = len(matrix)
cols = len(matrix[0])
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)
print("Transpose Matrix:")
for row in transpose:
    print(row)