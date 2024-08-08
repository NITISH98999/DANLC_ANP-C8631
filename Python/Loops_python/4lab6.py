# Q6. Wap to find the binary number of the given integer.
# 1.   Input a number
# 2.   Find the modulus of this number by 2 and save it into a array
# 3.   After the loop is finished, print the array in reverse.
n = int(input("Enter a number: "))
a = ""
while n > 0:
     a = str(n%2) + a
     n = n//2
print("The binary number is", a[::-1])
