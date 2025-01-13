student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}

for key, value in student.items():
    print(key, value)

print(student)
print(student["name"]) # John
print(student["courses"]) # ['Math', 'CompSci']
print(student["courses"][1]) # CompSci

student["phone"] = "555-5555"
print(student) # {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

student["name"] = "Jane"
print(student) # {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

del student["age"]
print(student) # {'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}