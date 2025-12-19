import string 

def encode(plain_text):
    trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz','zyxwvutsrqponmlkjihgfedcba', string.punctuation + ' ')
    plain_text = plain_text.lower()
    encoded = plain_text.translate(trans_table)

    result = " ".join(encoded[i:i+5] for i in range(0, len(encoded), 5))
    return result


def decode(ciphered_text):
    trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz','zyxwvutsrqponmlkjihgfedcba', string.punctuation + ' ')
    ciphered_text = ciphered_text.lower()
    decoded = ciphered_text.translate(trans_table)

    return decoded
