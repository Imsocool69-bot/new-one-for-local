seasons = ("Spring", "Summer", "Autumn", "Winter")
try:
    month = int(input("enter your number (from 1 to 12): "))
    if month < 1 or month > 12:
        print("Bro, Have you read the instructor yet?")
    elif month in (12, 1, 2):
        print("Season:", seasons[3])
    elif month in (3, 4, 5):
        print("Season:", seasons[0])
    elif month in (6, 7, 8):
        print("Season:", seasons[1])
    elif month in (9, 10, 11):
        print("Season:", seasons[2])
except ValueError:
    print("Are you serious-_-?")