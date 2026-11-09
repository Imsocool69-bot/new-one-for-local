L = []
while True:
    N = input("Enter number: ")
    if N != "":
        try:
            N = int(N)
            L.append(N)
        except ValueError:
            print("wrong value")
    elif N == "":
        break
L.sort(reverse = True)
print(L[0:6])