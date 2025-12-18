def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    sumofdiv = 1
    
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            sumofdiv += i
            if i != number // i:
                sumofdiv += number // i

    if sumofdiv == number:
        return "perfect"
    elif sumofdiv > number:
        return "abundant"
    else:
        return "deficient"
