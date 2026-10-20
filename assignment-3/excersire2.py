while True:
    i = float(input("Enter length in inches (negative number to quit): "))
    if i < 0:
        print("Program ended.")
        break
    c = i * 2.54
    print(i, "inches =", c, "cm")