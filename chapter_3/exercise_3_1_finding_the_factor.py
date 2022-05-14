def common_factors(num1, num2):
    """returns a list of the common factor of two num"""
    factorlist1 = []
    factorlist2 = []
    common_list = []
    for i in range(1, num1 +1):
        if num1 % i == 0:
            factorlist1.append(i)
    for i in range(1, num2 +1):
        if num2 % i == 0:
            factorlist2.append(i)
    for i in factorlist1:
        if i in factorlist2:
            common_list.append(i)
    return common_list






