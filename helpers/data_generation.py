import random
import string


def generate_random_integer(begin=1, end=100):
    return random.randint(begin, end)


def generate_random_string_with_digits(max_string_len=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(max_string_len))
