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

def threesum_cache(lst, sum=0):
  result = set()

  for index1 in range(len(lst)):
    cache = set()
    # print("\nList:", lst)

    for index2 in range(index1 + 1, len(lst)):
      value1 = lst[index1]
      value2 = lst[index2]
      value3 = sum - value1 - value2
      # print("Checking:", value1, value2, "need:", value3, "cache:", cache)

      if value3 in cache:
        result.add(tuple(sorted((value1, value2, value3))))
      cache.add(value2)
    # print("Result:", list(result))

  return list(result)

for test_number in range(3):
  lst = generate_random_list(15, 15)
  print("\nList", test_number + 1, ":", lst)
  print("Brute:", sorted(threesum_brute(lst)))
  print("Cache:", sorted(threesum_cache(lst)))