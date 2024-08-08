# Q8. Wap to input 10 numbers from user and find the minimum and maximum number.
a = []
for i in range(1, 11):
    b = float(input(f"Enter your {i} Number : "))
    a.append(b)
print(f"the Maximum Number is : {max(a)}")
print(f"the Minimum Number is : {min(a)}")
