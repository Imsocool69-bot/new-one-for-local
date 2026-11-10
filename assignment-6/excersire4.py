import string
def W_F(text, target_word):
    count = {}
    for word in text.lower().strip():
        word = word.strip(string.punctuation)
        if word:
            count[word] = count.get(word, 0) + 1
    target_word = target_word.strip(string.punctuation).lower()
    return count.get(target_word, 0)
text = input("enter your text:")
target = input("which word do you want to count?")
frequency = W_F(text, target)
if frequency == 1:
    print("the word:", target, "appear 1 time.")
elif frequency > 1:
    print("the word:", target, "appears", frequency, "times")