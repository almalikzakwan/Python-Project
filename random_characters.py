import random
import string 
from enum import Enum

class t(Enum):
    punctuation = 1
    punctuations = 2

def punctuation(type):
    match type:
        case t.punctuation:
            return random.choice(string.punctuation)
        case t.punctuations:
            return string.punctuation
        
def random_characters(k=64):
    ascii_letter = string.ascii_letters
    hexdigits = string.hexdigits
    # random_characters = ascii_letter + ''.join(punctuations) + hexdigits
    punctuations = punctuation(t.punctuation)
    random_characters = ascii_letter + hexdigits + punctuations
    # return pub_key + punctuation + ''.join(random.choices(list(random_characters), k=k))
    return ''.join(random.choices(list(random_characters), k=k))

print(random_characters())

