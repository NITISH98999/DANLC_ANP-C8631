# 3. Write a function in Python to count uppercase character in a text file “ABC.txt”
with open("C:\\Users\\DELL\\PycharmProjects\\project 1\\ABC.txt") as file:
    file1 = file.read()
count = 0
for char in file1:
    if char.isupper():
        count += 1
print(f"total no. of upper case : {count}")
