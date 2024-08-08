# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list: [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Split the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])
Original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split = []
first = Original_list[:3]
second = Original_list[3:]
split.append(first)
split.append(second)
print(split)
