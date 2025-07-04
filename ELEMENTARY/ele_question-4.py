#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
while True:
    answer = ""
    n = int(input("Please enter any number: "))
    
    if n == 0:
        print(n)
        exit()
    
    for i in range(1, n+1):
        answer += "{}".format(i)
        if i != n:
            answer += "+"
    answer += " = {}".format(sum(range(n+1)))
    print(answer)
    exit()