# Q4. Create Following Patterns using functions in a single program:-
# 1
# 22
# 333
# 4444
# 55555
print("Pattern 1 : ")
row = 5
for r in range(1, row + 1):
    for c in range(1, r + 1):
        print(r, end="")
    print()

# 1
# 12
# 123
# 1234
# 12345
print("Pattern 2 : ")
row = 5
for r in range(1, row + 1):
    for c in range(1, r + 1):
        print(c, end="")
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
print("Pattern 3 : ")
row = 5
num = 1
for r in range(1, row + 1):
    for c in range(1, r + 1):
        print(num, end=" ")
        num += 1
    print()

# 1
# 21
# 321
# 4321
# 54321
print("Pattern 4 : ")
row = 5
for r in range(1, row + 1):
    for c in range(r, 0, -1):
        print(c, end=" ")
    print()

#     1
#    12
#   123
#  1234
# 12345
print("Pattern 5 : ")
row = 5
for r in range(1, row + 1):
    for s in range(5, r - 1, -1):
        print(" ", end=" ")
    for c in range(1, r + 1):
        print(c, end=" ")
    print()
# 54321
# 4321
# 321
# 21
# 1
print("Pattern 6 : ")
row = 5
for r in range(1, row + 1):
    for c in range(row, r - 1, -1):
        print(c, end=" ")
    print()
# 12345
#  1234
#   123
#    12
#     1
print("Pattern 7 : ")
row = 5
for r in range(row, 0, -1):
    for s in range(row, r, -1):
        print(" ", end="")
    for c in range(1, r + 1):
        print(c, end="")
    print()
#          1
#        1 2 1
#      1 2 3 2 1
#    1 2 3 4 3 2 1
#  1 2 3 4 5 4 3 2 1
#    1 2 3 4 3 2 1
#      1 2 3 2 1
#        1 2 1
#          1
print("Pattern 8 : ")
row = 5
for r in range(1, row + 1):
    for s in range(5, r, -1):
        print(end="  ")
    for c in range(1, r + 1):
        print(c, end=" ")
    for c1 in range(c - 1, 0, -1):
        print(c1, end=" ")
    print()
for r in range(4, 0, -1):
    for s in range(5, r, -1):
        print(end="  ")
    for c in range(1, r + 1):
        print(c, end=" ")
    for c1 in range(c - 1, 0, -1):
        print(c1, end=" ")
    print()
#         5
#       5 4 5
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5
#   5 4 3 2 3 4 5
#     5 4 3 4 5
#       5 4 5
#         5
print("Pattern 8 : ")
row = 5
for i in range(1, row + 1):
    for _ in range(row - i):
        print(" ", end=" ")
    for j in range(row, (row + 1) - i, -1):
        print(j, end=" ")
    for j in range(row - i + 1, row + 1):
        print(j, end=" ")
    print()
for i in range(row - 1, 0, -1):
    for _ in range(row - i):
        print(" ", end=" ")
    for j in range(row, (row + 1) - i, -1):
        print(j, end=" ")
    for j in range(row - i + 1, row + 1):
        print(j, end=" ")
    print()

# 1
# 21
# 321
# 4321
# 54321
print("Pattern 9 : ")
rows = 5
for r in range(1, rows + 1):
    for c in range(r, 0, -1):
        print(c, end=" ")
    print()

# 5
# 45
# 345
# 2345
# 12345
print("Pattern 10 : ")
rows = 5
for r in range(rows, 0, -1):
    for c in range(r, rows + 1):
        print(c, end=" ")
    print()

print("Pattern 11 : ")
# 12345
# 2345
# 345
# 45
# 5
rows = 5
for r in range(1, rows + 1):
    for c in range(r, rows + 1):
        print(c, end=" ")
    print()

print("Pattern 12 : ")
# 54321
#  5432
#   543
#    54
#     5
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

