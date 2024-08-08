# 5. wap to copy the contents of one file into another. input both file names with path from user
src= input("Enter the Source of file : ")
dest = input("Enter the destination of file : ")

file1 = open(src,"r")
file2 = open(dest,"w")

text = file1.read()
file2.write(text)

print("file Copied Successfully!! ")

file1.close()
file2.close()


