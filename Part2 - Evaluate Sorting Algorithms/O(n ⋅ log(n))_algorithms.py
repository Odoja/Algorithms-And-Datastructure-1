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

def quick_sort():
  