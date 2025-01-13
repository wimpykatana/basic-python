numbers = {1,2,3,4,5}

print(numbers) # {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers) # {1, 2, 3, 4, 5, 6}

numbers.remove(3)
print(numbers) # {1, 2, 4, 5, 6}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#union
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8}

#intersection
print(set1 & set2) # {4, 5}

#difference
print(set1 - set2) # {1, 2, 3}
print(set2 - set1) # {8, 6, 7}