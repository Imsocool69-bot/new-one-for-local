numbers = []
while True:
    user_input = input("Enter a number (press Enter to finish): ").strip()
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("That is not a valid number. Try again.")
numbers.sort(reverse=True)
top_five = numbers[:5]
print("The five greatest numbers are:")
for number in top_five:
    print(f"{number:g}")