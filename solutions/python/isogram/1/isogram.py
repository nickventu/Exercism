def is_isogram(string):
    from collections import Counter
    string = string.replace(' ', '').replace('-','')
    count = Counter(string.lower())
    
    return all(v <= 1 for v in count.values())