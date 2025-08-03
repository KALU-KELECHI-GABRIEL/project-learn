#Write a function that checks whether an element occurs in a list.
def check_list(element, list):
    return element in list

num = [1, 2, 34, 67, 99, 3000, 35]

if check_list(38, num):
    print("Yes")
else:
    print("No")