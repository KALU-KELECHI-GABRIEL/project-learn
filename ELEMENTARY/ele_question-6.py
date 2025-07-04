#Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n
def product_n(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Input an integer: "))
option = input("Choose 'sum' or 'product': ")

if option == 'sum':
    result = sum_n(n)
    print(f"The sum of numbers from 1 to {n} is: {result}")
elif option == 'product':
    result = product_n(n)
    print(f"The product of numbers from 1 to {n} is: {result}")
else:
    print("Invalid option")