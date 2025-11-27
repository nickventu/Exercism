def response(hey_bob):
    
    stripped = hey_bob.strip()
    
    if not stripped:
        return "Fine. Be that way!"
    
    if '?' in stripped[-1] and stripped.isupper():
        return "Calm down, I know what I'm doing!"
    elif '?' in stripped[-1]:
        return "Sure."
    elif stripped.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."