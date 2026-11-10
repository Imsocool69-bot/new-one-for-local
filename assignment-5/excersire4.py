def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
my_list = []
while True:
    user_input = input("Enter a number (press Enter to finish): ")
    if user_input == "":
        break
    try:
        number = int(user_input)
        my_list.append(number)
    except ValueError:
        print("Please enter a valid number.")
result = calculate_sum(my_list)
print("Original list:", my_list)
print("Sum:", result)
