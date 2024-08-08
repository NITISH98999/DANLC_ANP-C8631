# Q4. Wap to print the factorial of a number.
# N=6  fact= 6*5*4*3*2*1
b = 1
a = int(input("Enter a NUMBER : "))
for i in range(a,0,-1):
    b = b * i
print(b)
