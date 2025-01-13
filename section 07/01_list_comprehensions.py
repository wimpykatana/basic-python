# List comprehensions 
# provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operation applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

# [expression for item in iterable if condition]

squares = [x**2 for x in range(10)]
print(squares)

even = [x for x in range(10) if x % 2 == 0]
print(even)

odd = [x for x in range(10) if x % 2 != 0]
print(odd)