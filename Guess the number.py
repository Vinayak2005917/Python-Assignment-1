import random
a = random.randint(0,10)

print("Guess the number!!")
print("The number is between 1 and 10")

while True:
    g = int(input(">> "))
    if g > a:
        print("Think smaller")
    elif g < a:
        print("Think larger")
    elif g == a:
        print("Correct guess!! The number is indeed ",a)
        break
