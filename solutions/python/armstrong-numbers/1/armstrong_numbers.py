def is_armstrong_number(number):
    s = str(number)
    digits = [int(d) for d in s]
    num_digits = len(s)
    sum = 0
    for i in digits:
        sum += i ** num_digits

    return number == sum