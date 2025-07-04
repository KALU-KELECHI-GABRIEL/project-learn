#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
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