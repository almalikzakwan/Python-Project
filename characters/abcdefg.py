import string
import time
import random

character = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

characters = character + digits + punctuation

printables = string.printable

count = 1
while count <= 3:
    
    print(''.join(random.choices(characters, k=64)))

# for string in characters + digits + punctuation:
#     print(string)
#     time.sleep(1)
