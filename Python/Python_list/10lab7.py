# 7. Write a function `transpose(matrix)` that takes a matrix (list of lists) and returns its transpose.
list = [[2, 5], [8, 3], [6, 8], [4, 3]]
b = []
for r in range(0, 2):
    cols = []
    for c in range(0, 4):
        cols.append(list[c][r])
    b.append(cols)
print(b)
print("New Transposed list")
for r in range(0, len(b)):
    for c in range(0, len(b[r])):
        print(b[r][c], end="\t")
    print()
