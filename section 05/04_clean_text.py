import re

def clean_text(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = " ".join(text.split())
    return text.lower()

# Example usage
text = "  Hello, World. ! This is a test.       "
cleaned_text = clean_text(text)
print(cleaned_text)  # hello world this is a test