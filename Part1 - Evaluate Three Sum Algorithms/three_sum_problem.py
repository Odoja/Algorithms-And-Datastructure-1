import random

def generate_random_list(list_lenght, list_size):
  return [random.randint(-10 * list_size, 10 * list_size) for _ in range(list_lenght)]

def threesum_brute(lst, sum=0):
  result = set()
  for index1 in range(len(lst)):
    for index2 in range(index1 + 1, len(lst)):
      for index3 in range(index2 + 1, len(lst)):
        if lst[index1] + lst[index2] + lst[index3] == sum:
          result.add(tuple(sorted((lst[index1], lst[index2], lst[index3]))))
  return list(result)

