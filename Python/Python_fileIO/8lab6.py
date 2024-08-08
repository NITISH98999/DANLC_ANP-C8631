# 6. Wap to search a particular word in a file and also prints number of occurrences.
Sstr = input("Enter a Word : ").lower()
count = 0
with open("story.txt","r")as file :
    text = file.read()
    word = text.lower().split()
    for i in word:
        if i == Sstr:
            count += 1
    if count != 0:
        print(f"Word Found {count} times!! ")
    else:
        print("Word Not Found!! ")

