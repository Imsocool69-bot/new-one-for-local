print("this function can say is this year leap or not.")
print("please only enter integer numbers.")
def check_leap_year():
        y = int(input("enter your favorite year: "))
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            print("this is a leap year.")
        else:
            print("this isn't a leap year.")
check_leap_year()