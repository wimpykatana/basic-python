def is_palindrome(word):
    word = "".join(word.lower() for word in word if word.isalnum())
    return word == word[::-1] # [::-1] reverses the string

def print_palindrome(word):
    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")


words = input("Enter a word: ")
print_palindrome(words)