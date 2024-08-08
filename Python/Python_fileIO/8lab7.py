# 7. Wap to search a string and replace it with another string (all occurrences)
filename = input("Enter FilePath : ")
file = open(filename, "r")
if file:
    print("file found")
    stext = input("Enter search value : ")
    rtext = input("Enter replace value : ")
    data1 = file.read()
    data = data1.split()
    count = 0
    for s in data:
        if stext == s:
            count += 1
    if count == 0:
        print("Value not found!!")
    else:
        print("Value found in File Successfully!!")
        print("Count of occurrences : ", count)
        ndata = data1.replace(stext, rtext)
        file1 = open(filename, "w")
        n = file1.write(ndata)
        file1.close()
        print("data replaced successfully!!", n)
else:
    print("File not found")
file.close()
