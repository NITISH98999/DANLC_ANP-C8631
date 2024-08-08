# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
try:
    b= a/b
except ZeroDivisionError as file:
    print(file,"!!")
print(b)
