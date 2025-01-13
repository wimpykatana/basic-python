def count_words_and_lines(file_path):
    try:
        with open(file_path) as file:
            lines = file.readlines()
            words = sum(len(line.split()) for line in lines)
            print(f'Number of words: {words}')
            print(f'Number of lines: {len(lines)}')
    except FileNotFoundError:
        print(f"File {file_path} not found")

count_words_and_lines('sample.txt')