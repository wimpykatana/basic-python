numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
mixed = [1, 'apple', True, 3.14]

print(numbers[2])  # 3
print(fruits[1])  # banana
print(mixed[3])  # 3.14
print(fruits[-1]) # elderberry

slice_fruits = fruits[1:4]
print(slice_fruits)  # ['banana', 'cherry', 'date']

print(fruits[-1])  # elderberry

fruits.append('grape')
print(fruits) # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'grape']
fruits.insert(2, 'manggo')
print(fruits)  # ['apple', 'banana', 'manggo', 'cherry', 'date', 'elderberry', 'grape']

fruits.remove('banana')
print(fruits)  # ['apple', 'manggo', 'cherry', 'date', 'elderberry', 'grape']

del fruits[3]
print(fruits)  # ['apple', 'manggo', 'cherry', 'elderberry', 'grape']

fruits.pop()
print(fruits)  # ['apple', 'manggo', 'cherry', 'elderberry']
