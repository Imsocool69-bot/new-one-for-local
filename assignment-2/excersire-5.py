import math
def unit_price(diameter_cm, price):
    radius_m = diameter_cm / 200
    return price / (math.pi * radius_m ** 2)
d1, p1 = float(input("Pizza 1 diameter (cm): ")), float(input("Pizza 1 price ($): "))
d2, p2 = float(input("Pizza 2 diameter (cm): ")), float(input("Pizza 2 price ($): "))
u1, u2 = unit_price(d1, p1), unit_price(d2, p2)
print(f"Pizza 1: ${u1:.2f}/m²")
print(f"Pizza 2: ${u2:.2f}/m²")
if u1 < u2:
    print("🏆 Winner: Pizza 1")
elif u2 < u1:
    print("🏆 Winner: Pizza 2")
else:
    print("🤝 It's a tie!")