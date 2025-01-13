#split()
text = "Python is fun"
words = text.split()
print(words)  # Output: ['Python', 'is', 'fun']

text2 = "Python,is,fun"
words2 = text2.split(",")
print(words2)  # Output: ['Python', 'is', 'fun']

#join()
words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)  # Output: Python is fun

sentence = "_".join(words)
print(sentence)  # Output: Python_is_fun

#replace()
text = "Java is fun"
updated_text = text.replace("Java", "Python")
print(updated_text)  # Output: Python is fun

#strip()
messy_text = "      tHIS is A vEry MessY TexT    "
cleaned_text = messy_text.strip().lower()
print(cleaned_text)  # Output: this is a very messy text
