import random
i = random.randint(1, 10)
while True:
    g = int(input("Guess a number between 1 and 10: "))
    if g > i:
        print("Too high")
    elif g < i:
        print("Too low")
    else:
        print("Correct")
        break