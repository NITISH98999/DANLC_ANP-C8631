# Q9. Wap to print all the leap years from 1 to n.
# Input n from the user
n = int(input("Enter a number: "))
print(f"Leap years from 1 to {n} : ")
for i in range(1, n + 1):
    if (i % 4 == 0):
        print(i)
