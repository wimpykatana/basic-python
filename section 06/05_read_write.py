def write(file_path, text):
    with open(file_path, 'w') as f:
        for line in text:
            f.write(line + '\n')

def read(file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print(f"File {file_path} not found")

fruits = ['apple', 'banana', 'cherry', 'tomato']
write('sample_text.txt', fruits)
read('sample_text.txt')