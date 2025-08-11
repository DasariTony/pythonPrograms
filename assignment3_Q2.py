# login Authentication Program 
user_name=input("Enter user_name:")
Password=int(input("Enter Password:"))
if user_name=="Tony" and Password==123:
    print("Both user_name and Password are Correct")
elif user_name=="Tony" and Password!=123:
    print("user_name is correct but Password is incorrect")
elif user_name=="Tony":
    print("user_name is correct")
else:
    print("Thank You")