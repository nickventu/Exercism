def answer(question):

    if not question.startswith('What is '):
        raise ValueError("syntax error")
        
    question = (question.replace('What is ', '')
                        .replace('plus', '+')
                        .replace('minus','-')
                        .replace('multiplied by', '*')
                        .replace('divided by', '/')
                        .replace('?', '')
               )
    
    tokens = question.split()
    
    if not tokens:
        raise ValueError("syntax error")
    if tokens[0] in ["+","-","*","/"]:
        raise ValueError("syntax error")
    try:
        result = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        if operator not in ["+", "-", "*", "/"]:
            if operator.isdigit() or (operator.startswith('-') and operator[1:].isdigit()):
                raise ValueError("syntax error")
            raise ValueError("unknown operation")
        if i + 1 >= len(tokens):
            raise ValueError("syntax error")
        try:
            next_val = int(tokens[i + 1])
        except ValueError:
            raise ValueError("syntax error")

        if operator == "+": result += next_val
        elif operator == "-": result -= next_val
        elif operator == "*": result *= next_val
        elif operator == "/": result /= next_val

    return result
            