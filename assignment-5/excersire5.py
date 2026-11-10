def RON(num):
    even_nums = [number for number in num if number % 2 == 0]
    return even_nums
numbers = []
while True:
    original_list = input("Enter your numbers (press Enter to quit): ")
    if original_list == "":
        break
    try:
        number = int(original_list)
        numbers.append(number)
    except ValueError:
        print("That is not a valid input. Try again.")
cutdown = RON(numbers)
print("Original list:", numbers)
print("Low-budget list:", cutdown)
