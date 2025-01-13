try:
    with open('sample.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('File not found')
    