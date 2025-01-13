# lamda is a small anonymous function
# lambda arguments: expression
from functools import reduce

add = lambda a, b: a + b
val = add(10, 20)
print(val) # Output: 30

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

sum = reduce(lambda a, b: a + b, numbers)
print(sum)  # Output: 55