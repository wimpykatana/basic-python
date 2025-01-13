with open('sample.txt', 'w') as f:
    f.write('Hello, world!')
    f.writelines(['\nalice','\nbob','\ncharlie'])

#automatically closes the file when the block is exited