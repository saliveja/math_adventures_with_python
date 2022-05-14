from random import randint

def numberGame():
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("What's your guess\n"))
    while guess:
        if number == guess:
            print(f"That's correct! The number was {number}")
            break
        elif number > guess:
            print("Nope. Higher.")
        else:
            print("Nope. Lower.")
        guess = int(input("What's your guess\n"))

numberGame()


# def greet():
#     name = input("What is your name?")
#     # print(F"Hello, {name}")
#     if name.lower() == 'peter':
#         print("That's my name too!")
#     else:
#         print(f"Hello, {name.title()}")
#
# greet()