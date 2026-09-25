import random

def generate_random_list(list_lenght, list_size):
    return [random.randint(0, 10 * list_size) for _ in range(list_lenght)]