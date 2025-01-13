setence = input("Enter a sentence: ")
words = setence.split()

word_count = {}

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count:", word_count)