# 3. Write a Python program to Check if two sets have any elements in common. If
# yes, display the common elements.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# Output:
# {10}
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common = set1.intersection(set2)
print(common)
