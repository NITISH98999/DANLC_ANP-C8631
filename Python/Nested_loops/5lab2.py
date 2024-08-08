# Q2. Wap to print all the Armstrong numbers between a given range.
start_range = int(input("Enter a start Number: "))
end_range = int(input("Enter a end Number: "))
print("The Armstrong numbers between this range are: ")
for num in range(start_range, end_range+1):
    string_num = str(num)
    length = len(string_num)
    sum_of_nums = 0
    for digit in string_num:
        sum_of_nums += int(digit) ** length
    if sum_of_nums == num:
      print(num,end=',')
