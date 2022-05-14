from random import randint

def numberGame():
    number = randint(1, 100)

def greet():
    name = input("What is your name?")
    # print(F"Hello, {name}")
    if name.lower() == 'peter':
        print("That's my name too!")
    else:
        print(f"Hello, {name.title()}")

greet()