numbers = []
while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")