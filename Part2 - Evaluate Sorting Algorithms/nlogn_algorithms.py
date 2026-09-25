def merge_sort(list_):
  length = len(list_)

  if length <= 1:
    return list_

  # Ex. splits the list into two halves [5, 2, 2, 5] -> [5, 2] and [2, 5]
  mid = length // 2
  # E.x [5,2] gets declared as left_side and [2,5] gets declared as right_side
  left_side = list_[:mid]
  right_side = list_[mid:]

  # Recursively calls merge_sort until the list is split into single elements.
  sorted_left = merge_sort(left_side)
  sorted_right = merge_sort(right_side)

  return merge(sorted_left, sorted_right)

def merge(left_value, right_value):
  list_ = []
  left_index, right_index = 0, 0

  while left_index < len(left_value) and right_index < len(right_value):
    if left_value[left_index] < right_value[right_index]:
      # Add left value to list.
      list_ += [left_value[left_index]]
      left_index += 1
    else:
      # Add right value to list.
      list_ += [right_value[right_index]]
      right_index += 1

  while left_index < len(left_value):
    # Add left value to list.
    list_ += [left_value[left_index]]
    left_index += 1
  
  while right_index < len(right_value):
    # Add right value to list.
    list_ += [right_value[right_index]]
    right_index += 1

  return list_

def quick_sort(list_):
  length = len(list_)
  
  if length <= 1:
    return list_
  
  first_number, left_list, right_list = partition(list_)

  # Recursively calls quick_sort until the list is split into 2 containing single elements
  # Those smaller than the first number to the left and those larger to the right.
  sorted_left = quick_sort(left_list)
  sorted_right = quick_sort(right_list)

  return sorted_left + [first_number] + sorted_right

def partition(list_):
  length = len(list_)

  first_number = list_[0]
  left_list, right_list = [], []

  for index in range(1, length):
    secound_number = list_[index]
    # Compare the secound number with the first number and place it in the left or right list.
    if secound_number <= first_number:
      left_list += [secound_number]
    else:
      right_list += [secound_number]
  return first_number, left_list, right_list

