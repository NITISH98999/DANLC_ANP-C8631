# 3. Write a Python program to reverse words in a string
# String = “Deeptech Python Training”
String = input("Enter a String : ")
str1= String.split()
for i in str1:
    print(i[::-1],end=" ")
