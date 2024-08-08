# 10. Write a function `rotate_list(lst, k)` that rotates a list to the right by `k` positions. For example,
# `rotate_list([1, 2, 3, 4, 5], 2)` should return `[4, 5, 1, 2, 3]`.
def rotate_list(list, k):
    return list[-k:] + list[:-k]


result = rotate_list([1, 2, 3, 4, 5], 2)
print(result)