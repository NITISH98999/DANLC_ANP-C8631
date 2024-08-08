#5. Wap to check a character and print whether it is an alphabet, number or Special character.
t=ord(input("Enter any value"))
if t>31 and t<48 :
    print("its character")
if t>47 and t<58 :
    print("Its a Number")
if t>64 and t<123 :
    print("its an Alphabet")
