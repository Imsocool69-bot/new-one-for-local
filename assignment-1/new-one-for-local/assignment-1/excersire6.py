def ex_mass():
    talents = float(input("enter your talent (number only): "))
    pounds = float(input("enter your pounds: "))
    lots = float(input("enter your lots: "))
    total_gram = ((talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3))
    kilograms = int(total_gram // 1000)
    grams = total_gram % 1000
    print("modern weight is:", kilograms, "kilograms and", grams, "grams")
ex_mass()
