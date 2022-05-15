def average(a, b):
    return (a + b) / 2

def squareRoot(num, low, high):
    """Finds the square root of num by playing the number guessing game
    strategy by guessing over the range from 'low to 'high"""

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

squareRoot(200, 14, 15)
# 14.142136573791504

squareRoot(1000, 100, 110)
# 100.00000953674316

squareRoot(50000, 250, 500)
# 250.0002384185791