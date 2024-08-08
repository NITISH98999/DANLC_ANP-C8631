print("pyramid pattern ")
row = int(input("enter number of rows:"))
for i in range(1, row + 1):
    print("*" * i)


print("inverted half pyramid ")
row = int(input("enter number of rows:"))
for i in range(row, 0, -1):
    print("*" * i)


print("hollow full pyramid ")
def hlwFullPyramid(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if i == rows - 1 or j == 0 or j == 2 * i:   #
                print("*", end="")
            else:
                print(" ", end="")
        print()
hlwFullPyramid(8)


print("pyramid")
def full_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print()
full_pyramid(5)

print("hollow half")
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()
number_of_rows = 5
print_number_pyramid(number_of_rows)


print("alphabet")
for r in range(65,91):
    for s in range(90, r, -1):
        print(end="  ")
    for c in range(65, r+1):
        print(chr(c), end=" ")
    for c1 in range(c-1, 64, -1):
        print(chr(c1), end=" ")
    print()