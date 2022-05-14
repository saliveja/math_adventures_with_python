# factor is a number that can evenly divide an integer
def factors(num):
    """returns a list of the factors of num"""
    factorlist = []
    for i in range(1, num +1):
        if num % i == 0:
            # if a number is a factor,
            # num % i = 0
            # ie. 5 is a factor of 10
            factorlist.append(i)
            # if this condition is met
            # we add the factor to the factorlist
    return factorlist
    # and return the list

