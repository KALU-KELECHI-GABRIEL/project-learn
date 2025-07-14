#Modify the previous program such that only the users Alice and Bob are greeted with their names.
name = input("Please input your name: ")

if name.lower() == "alice" or name.lower() == "bob":
    print(f"Good Afternoon, {name}")
else:
    print("Good Afternoon")