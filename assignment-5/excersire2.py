import math
T = True
while True:
    N = int(input("Enter the number: "))
    if N < 2:
        print("N is not a prime number")
    elif N == 2:
        print("N is a prime number")
    else:
        A = (round(math.sqrt(N)))
        for i in range(2, int(A) + 1):
            if N % i != 0:
                T = True
            elif N % i == 0:
                T = False
                break
        if T == True:
            print("N is a prime number")
        elif T == False:
            print("N is not a prime number")