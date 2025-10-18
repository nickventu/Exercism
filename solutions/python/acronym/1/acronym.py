def abbreviate(words):

    words = words.replace('-',' ').replace('_',' ')
    acronym = ""
    for word in words.split():
        print(word[0])
        acronym += word[0]
    acronym = acronym.upper()
    return acronym
        
    
