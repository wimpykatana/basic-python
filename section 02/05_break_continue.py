for i in range(10):
    if i == 5:
        break
    print(i)
print("Keluar dari loop")

for i in range(10):
    if i == 5:
        continue
    print(i)
print("Keluar dari loop")

# contoh penggunaan continue untuk bilangan ganjil
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)