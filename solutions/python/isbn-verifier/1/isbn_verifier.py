def is_valid(isbn):

    if not isbn:
        return False
        
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    lastc = isbn[-1]
    if lastc == 'X':
        last = 10
    elif lastc.isdigit():
        last = int(lastc)
    else:
        return False

    isbn = isbn[:-1]
    if not isbn.isdigit():
        return False
        
    total = 0
    for n in range(9):
        total += int(isbn[n]) * (10 - n)
    total += last * 1
    
    return (total % 11) == 0