# 2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
with open("C:\\Users\\DELL\\PycharmProjects\\project 1\\ABC.txt","r") as file :
    file1 = file.read()
split = file1.split()
count = len(split)
print(f"total Number of words : {count}")


