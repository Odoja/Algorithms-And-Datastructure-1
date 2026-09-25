import random

def generate_random_list(list_lenght, list_size):
    return [random.randint(0, 10 * list_size) for _ in range(list_lenght)]

def bucket_sort(list_):
  # Check if list is empty
  if not list_:
    return list_
  number_of_buckets = len(list_)
  lowest_value_number = min(list_) 
  highest_value_number = max(list_)

  # Create one empty bucket per number in list.
  buckets = [[] for _ in range(number_of_buckets)]

  # Places each number in the list into a bucket based on its value.
  # Ex. (5 - 4) / (50 - 4 + 1) * 10 = 0.21 -> int() removes the decimal = 0.
  for number in list_:
    index = int((number - lowest_value_number) / (highest_value_number - lowest_value_number + 1) * number_of_buckets)
    # Places in bucket index calculated in the example above 0.
    buckets[index].append(number)

  for bucket in buckets:
    bucket.sort()

  # "Empties" (removes) the buckets and places them in an ordered list.
  return [num for bucket in buckets for num in bucket]


def radix_sort():
   pass

list_ = generate_random_list(10, 10)
sorted_list = bucket_sort(list_)
print(sorted_list)