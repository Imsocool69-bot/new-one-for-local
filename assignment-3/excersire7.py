def create_acronym(phrase):
    w = phrase.split()
    a = "".join([word[0].upper() for word in w])
    return a
u = input("Enter a phrase: ")
r = create_acronym(u)
print("The acronym: ", r)