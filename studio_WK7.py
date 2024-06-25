counter = 0


def power_while(base, exponent):
    i = 0
    product = 1
    while i < exponent:
        product *= base
        i += 1
    return product


def power_for(base, exponent):
    product = 1
    for i in range(exponent):
        product *= base
    return product


def power_recursion(base, exponent):
    if exponent == 0:
        return base
    base *= base
    power_recursion(base, exponent - 1)


power_recursion(2, 3)
