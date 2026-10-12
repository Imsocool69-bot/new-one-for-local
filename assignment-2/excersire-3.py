print("this program is made for researching only!")
def sex_and_hemoglobin():
    s = input("enter your gender(male/female): ").strip()
    h = float(input("enter your hemoglobin: "))
    if s == "male":
        if h < 134.00:
            print("your hemoglobin is low.")
        elif h >= 134.00 and h < 167.00:
            print("your hemoglobin is normal.")
        else:
            print("your hemoglobin is high.")
    elif s == "female":
        if h < 117.00:
            print("your hemoglobin is low.")
        elif h >= 117.00 and h < 155.00:
            print("your hemoglobin is normal.")
        else:
            print("your hemoglobin is high.")
    else:
        print("invalid character!")

sex_and_hemoglobin()