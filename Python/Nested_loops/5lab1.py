# Q1. Wap to print first 10 prime numbers
count = 0
num = 2
while count < 10:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num,end=" ")
        count += 1
    num += 1
