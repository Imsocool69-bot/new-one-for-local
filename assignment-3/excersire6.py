def get_middle_character(text):
    l = len(text)
    m = l // 2
    if l % 2 == 0:
        return text[m - 1 : m + 1]
    else:
        return text[m]
u = input("Enter a string: ")
r = get_middle_character(u)
print("The middle character(s): ", r)