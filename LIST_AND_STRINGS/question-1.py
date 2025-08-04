#Write a function that returns the largest element in a list.
def max_element(a_list):
    assume = a_list[0]
    for i in range(1, len(a_list)):
        if a_list[i] > assume:
            assume = a_list[i]
    return assume

num = [1,2,34,67,80,23,45,6]
print(max_element(num))