import re
def sum_of_numbers_in_paragraph(text: str) -> int:
    numbers = re.findall(r"\d+", text)
    return sum(int(num) for num in numbers)
paragraph = input("enter your paragraph: ")
total = sum_of_numbers_in_paragraph(paragraph)
print("total number: ", total)