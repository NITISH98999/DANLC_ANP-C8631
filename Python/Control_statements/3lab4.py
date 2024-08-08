"""Wap to check if the user has provided the correct currency note for deposit or not.
The note should be in between the following currencies:
2000, 500, 200, 100, 50"""
curr=int(input("Enter your currency Note : "))
if curr==2000 or curr==500 or curr==200 or curr==100 or curr==50:
    print(" Currency Note is correct")
else:
    print("Enter Correct Currency Note!!!")
