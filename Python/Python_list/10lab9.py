# 9. Given two lists `a = [1, 2, 3]` and `b = [4, 5, 6]`,
# write code to merge them into a single list and then flatten a list of lists `c = [[1, 2], [3, 4], [5, 6]]` into a single list.
a = [1, 2, 3]
b = [4, 5, 6]
mergedlist = a + b
print("Merged list:", mergedlist)

c = [[1, 2], [3, 4], [5, 6]]
flattenedlist = sum(c, [])
print("Flattened list:", flattenedlist)
