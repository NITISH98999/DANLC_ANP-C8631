# 8. Given the list `numbers = [15, 3, 7, 20, 13, 9, 25, 1, 10]`,
# write a list comprehension to create a new list containing only the even numbers.
numbers = [15, 3, 7, 20, 13, 9, 25, 1, 10]
newlist = [ x for x in numbers if x %2 ==0]
print(newlist)
