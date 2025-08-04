#Write a program that prints all prime numbers.
def prime_numbers(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_numbers(l):
    for number in range(2, l + 1):
        if prime_numbers(number):
            print(number)
            
l = int(input("Enter a limit: "))
print(f"Prime Numbers up to {l} are: ")
print_prime_numbers(l)