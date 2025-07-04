#Write a program that prints a multiplication table for numbers up to 12
def multiplication_table(n):
    for i in range(1, n + 1):
        print(f"THe Multiplication Table of {i}: ")
        for j in range(1, 13):
            print(f"{i} x {j} = {i * j}")
        print("_" * 20)

multiplication_table(12)