# 4. Write a Python Count vowels in a string
# input= “Welcome to Python Assignment”
# Output: Total vowels are: 8
str = input("Enter a String : ")
vowels = "a,e,i,o,u,A,E,I,E,O,U"
vcount = 0
for ch in str:
    if ch in vowels:
        vcount += 1
print(f"Total no. of vowels are : {vcount}")
