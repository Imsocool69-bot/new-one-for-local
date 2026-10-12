print("this function only accept only numbers!")
def length_of_zander():
    Z = float(input("enter your zander's length(cm): "))
    if Z >= 42.00:
        print("acceptable size")
    elif Z < 42.00:
        print("release the fish back into the lake because your zander doesn't meet size limit")

length_of_zander()