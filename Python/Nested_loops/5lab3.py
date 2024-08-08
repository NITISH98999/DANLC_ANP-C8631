# Q3. Wap to print multiplication tables from a given range.
start = int(input("Enter a number: "))
end = int(input("Enter a number: "))
for num in range(start, end+1):
    print()
    print(f"Multiplication Table of {num}:")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
