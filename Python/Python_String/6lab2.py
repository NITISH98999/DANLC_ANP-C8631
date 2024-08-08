# 2. Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n"
String = "\nBest \nDeeptech \nPython \nTraining\n"
str1 = String.split("\n")
clean="".join(str1)
print(clean)
