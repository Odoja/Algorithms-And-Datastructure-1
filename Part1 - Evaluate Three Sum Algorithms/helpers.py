import random

def generate_random_list(list_lenght, list_size):
  return [random.randint(-10 * list_size, 10 * list_size) for _ in range(list_lenght)]