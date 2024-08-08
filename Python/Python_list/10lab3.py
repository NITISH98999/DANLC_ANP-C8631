# 3. Write a Python program to find duplicate values from a list and display those.
list2 = [5, 96, 4, 75, 85, 74, 5, 96, 5, 7]
list1 = []
for i in list2:
    if list2.count(i)>1 :
        list1.append(i)
print(f"duplicate values from a list are : {list1}")