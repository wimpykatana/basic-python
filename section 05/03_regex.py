import re

text = "contact me at: 123-456-7890"
digits = re.findall(r'\d+', text)
print(digits)  # ['123', '456', '7890']

updated_text = re.sub(r'\d', '*', text)
print(updated_text)  # contact me at: ***-***-***