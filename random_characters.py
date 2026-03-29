import random
import string 

def random_characters(k=16):
    all_punctuation = string.punctuation
    punctuations = random.choices(all_punctuation, k=16)
    punctuation = random.choice(all_punctuation)
    pub_key = f""
    ascii_letter = string.ascii_letters
    hexdigits = string.hexdigits
    # random_characters = ascii_letter + ''.join(punctuations) + hexdigits
    random_characters = ascii_letter + hexdigits
    # return pub_key + punctuation + ''.join(random.choices(list(random_characters), k=k))
    return pub_key + ''.join(random.choices(list(random_characters), k=k))

print(random_characters())
