def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = 54
print("Factorial of", num, "=", factorial(num))
