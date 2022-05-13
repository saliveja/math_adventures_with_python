
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
        running_sum += i
        # adding i to the running_sum every loop
    return running_sum

mySum(100)
