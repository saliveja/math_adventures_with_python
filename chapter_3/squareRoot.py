def average(a, b):
    return (a + b) / 2

def squareRoot(num, low, high):
    """Finds the square root of num by playing the number guessing game
    strategy by guessing over the range from 'low to 'high"""
    # num is the number we want the square root of
    # low, the lowest limit of the number
    # high, the highest limit of the number
    # square root is the number ** 2 (the number * itself, ie. 7*7)


    for i in range(20):
        # how many times we can guess
        guess = average(low, high)
        if guess ** 2 == num:
            print(guess)
        elif guess ** 2 > num:
            high = guess
        else:
            low = guess
    print(guess)

squareRoot(60, 7, 7.9)
# approximately 7.746