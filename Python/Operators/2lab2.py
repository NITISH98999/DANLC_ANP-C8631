#2.  Wap to check whether a character is  in lower case or upper case.
y = ord(input("Enter your character : "))
if 65 <= y <= 90:
    print("Given Character is Upper case")
elif 97 <= y <= 122 :
    print("Give Character is Lower Case")
else:
    print("Enter Correct Character !!!")
