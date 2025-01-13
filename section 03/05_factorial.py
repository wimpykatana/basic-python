def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # recursive call

def print_factorial(n):
    print(f"The factorial of {n} is {factorial(n)}")

print_factorial(5)