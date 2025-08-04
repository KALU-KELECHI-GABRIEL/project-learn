#Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.
import random

print(" ")
low_guess = int(input("Enter a lower bound: "))
high_guess = int(input("Enter a higher bound: "))
print(f"You have ten(10) chances to guess the number between {low_guess} and {high_guess}.")

cn = random.randint(low_guess, high_guess)
ch = 10
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))
    if guess == cn:
        print(f"Correct. The number is {cn}. You took {gc} attempts.")
        break
    elif gc >= ch and guess != cn:
        print(f"Sorry. You ran out of chances. The number was {cn}")
    elif guess > cn:
        print("Too high. Try again.")
    elif guess < cn:
        print("Too low. Try again.")