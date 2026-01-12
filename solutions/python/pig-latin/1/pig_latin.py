def translate(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []

    for word in text.split():  # split the phrase into words

        if word[0] in vowels or word.startswith(('xr', 'yt')):
            result.append(word + "ay")
            continue
        if word.startswith('y'):
            result.append(word[1:] + 'yay')
            continue 
            
        consonant_cluster = ""
        while word and word[0] not in vowels:
            if word.startswith('qu'):
                consonant_cluster += 'qu'
                word = word[2:]
            elif word.startswith('y'):
                break
            else:
                consonant_cluster += word[0]
                word = word[1:]
        result.append(word + consonant_cluster + "ay")

    return " ".join(result)
