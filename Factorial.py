def Factorial (a):
    if a == 0:
        return 1
    for i in range(1,a):
        a *= i
    return a
a = int(input("Enter the number:"))
print(f"The Factorial of {a} is {Factorial (a)}.")
