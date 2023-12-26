import random
import string

def generate_string(len: int):
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for _ in range(len)])

file = open("test.txt", "w")
file.write(generate_string(100000))
file.close()