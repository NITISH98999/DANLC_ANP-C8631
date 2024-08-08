# 1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
file = open("C:\\Users\\DELL\\Downloads\\how to use.txt","r")
line = file.readline()
for ch in file:
    print(ch.strip())