import random
def gamble():
    d1 = random.randint(0, 9)
    d2 = random.randint(0, 9)
    d3 = random.randint(0, 9)
    d4 = random.randint(1, 6)
    d5 = random.randint(1, 6)
    d6 = random.randint(1, 6)
    d7 = random.randint(1, 6)
    print ("3-digit code:", d1, d2, d3)
    print ("4-digit code:", d4, d5, d6, d7)
gamble()
