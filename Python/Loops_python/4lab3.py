# Q3. Wap to input  10 numbers from user and find their sum and average
a = 0
print("Enter any 10 Numbers : ")
for i in range(1, 11):
    a += int(input())
    #a += b
print(f"Sum of the 10 Number is : {a}")
print(f"Average of 10 Number is : {a / 10}")
