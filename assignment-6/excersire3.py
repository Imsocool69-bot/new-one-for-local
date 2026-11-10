names = set()
while True:
    name = input("Enter your name(press enter to finish):")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("Welcome to Earth server")
        names.add(name)
print("\nnames entered:")
for name in names:
    print(name)