def is_paired(input_string):

    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for c in input_string:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()

    return len(stack) == 0