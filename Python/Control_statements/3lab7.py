# 7. Input amount and print its denomination :-
# a. 2000X
# b. 500 X
# c. 200 X
# d. 100 X
# e. 50 X

amount = int(input("Enter amount : "))

if amount % 100 == 0:
    if amount >= 2000:
        notes = amount // 2000
        print(f"2000 X {notes} = {notes * 2000}")
        amount = amount - (notes * 2000)

    if amount >= 500:
        notes = amount // 500
        print(f"500 X {notes} = {notes * 500}")
        amount = amount - (notes * 500)

    if amount >= 200:
        notes = amount // 200
        print(f"200 X {notes} = {notes * 200}")
        amount = amount - (notes * 200)

    if amount >= 100:
        notes = amount // 100
        print(f"100 X {notes} = {notes * 100}")
        amount = amount - (notes * 100)
else:
    print("Amount should be multiple of 100!!")