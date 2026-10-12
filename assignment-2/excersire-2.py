print("This is cabin class selection. Only choose these 4 options:")
print("LUX: upper-deck cabin with a balcony.")
print("A: above the car deck, equipped with a window.")
print("B: windowless cabin above the car deck.")
print("C: windowless cabin below the car deck.")
def cabin():
    U = input("Enter your cabin class: ").strip()
    if U == "LUX":
        print("You selected LUX: upper-deck cabin with a balcony.")
    elif U == "A":
        print("You selected A: above the car deck, equipped with a window.")
    elif U == "B":
        print("You selected B: windowless cabin above the car deck.")
    elif U == "C":
        print("You selected C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
cabin()