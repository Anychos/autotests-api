import random
import string

def random_email():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + '@mail.ru'