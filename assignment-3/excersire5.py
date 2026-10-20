USERNAME = "python"
PASSWORD = "rules"
a = 0
m = 5

while a < m:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    
    if username_input == USERNAME and password_input == PASSWORD:
        print("Welcome")
        break
    else:
        a += 1
        print("Incorrect login. Remaining attempts: ", m - a)
else:
    print("Access denied")