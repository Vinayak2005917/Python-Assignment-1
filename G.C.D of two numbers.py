def GCD(a,b):
    while a%b != 0:
        t,a = a,b
        b = t%b
    return b
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the second number: "))
print(f"The G.C.D of {num1} and {num2} is {GCD(num1,num2)}")
