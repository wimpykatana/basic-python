def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: division by zero"
    else:
        return a / b
    

while True:
    print("\nSimple Calculator")
    print("Options:")
    print("Enter 1 to add")
    print("Enter 2 to subtract")
    print("Enter 3 to multiply")
    print("Enter 4 to divide")
    print("Enter 5 to exit")

    choice = input("Enter choice: ")

    if choice == '5':
        print("Exiting program")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("--------------------")
    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", sub(num1, num2))
    elif choice == '3':
        print("Result: ", mul(num1, num2))
    elif choice == '4':
        print("Result: ", div(num1, num2))
    else:
        print("Invalid input")
    print("--------------------")