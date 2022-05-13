
def average(a, b):
    return (a + b) / 2
    # using parenthesis makes sure addition is made before division

running_sum = 0
for i in range(10):
    running_sum += 3
print(running_sum)

def mySum(num):
    running_sum = 0
    # starting value for running_sum is 0
    for i in range(1, num + 1):
        # +1 for it to add 100 numbers not 99
        running_sum += i
        # adding i to the running_sum every loop
    return running_sum

mySum(100)

def mySum2(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i ** 2 +1

    return running_sum


