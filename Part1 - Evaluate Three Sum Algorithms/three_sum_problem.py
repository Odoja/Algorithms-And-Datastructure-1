import random

def generate_random_list(list_lenght, list_size):
  return [random.randint(-10 * list_size, 10 * list_size) for _ in range(list_lenght)]

def threesum_brute(list_, sum=0):
  length = len(list_)
  result = set()

  for index1 in range(length):
    for index2 in range(index1 + 1, length):
      for index3 in range(index2 + 1, length):
        if list_[index1] + list_[index2] + list_[index3] == sum:
          result.add(tuple(sorted((list_[index1], list_[index2], list_[index3]))))
  return list(result)

def threesum_cache(list_, sum=0):
  length = len(list_)
  result = set()

  for index1 in range(length):
    cache = set()
    # print("\nList:", list_)

    for index2 in range(index1 + 1, length):
      value1 = list_[index1]
      value2 = list_[index2]
      value3 = sum - value1 - value2
      # print("Checking:", value1, value2, "need:", value3, "cache:", cache)

      if value3 in cache:
        result.add(tuple(sorted((value1, value2, value3))))
      cache.add(value2)
    # print("Result:", list(result))

  return list(result)
