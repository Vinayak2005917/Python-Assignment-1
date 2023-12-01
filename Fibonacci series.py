a = int(input("Enter the number: "))
print(f"The fibonacci series starts with: ")
b =  0
c = 1
for i in range(a):
    print(b)
    b = b + c
    c = b - c
