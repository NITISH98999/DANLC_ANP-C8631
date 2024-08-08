# 1. Write a Python program to count the occurrences of each word in a
# given sentence
# string = “To change the overall look of your document. To change the look
# available in the gallery”
str = "To change the overall look of your document. To change the look available in the gallery"
word = input("Enter a Word : ")
count = 0
str1 = str.split()
for i in str1:
    if i == word:
        count += 1
print(f"occurrences of {i} : ",count)
