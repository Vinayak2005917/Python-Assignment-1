a = input("Enter your word/sentences: ")
def ispallindrium(a):
    if a == a[::-1]:
        return "It is Pallindrium"
    else:
        return "It is not a Pallindrium"
print(ispallindrium(a))
