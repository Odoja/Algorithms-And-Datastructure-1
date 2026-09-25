def selection_sort(list_):
  length = len(list_)

  for current_index in range(length - 1):
    index_of_smallest_value = current_index

    # Search the rest of the list for a smaller value.
    for compare_index in range(current_index + 1, length):
      if list_[compare_index] < list_[index_of_smallest_value]:
        index_of_smallest_value = compare_index
    # Swap the smallest value into the current index position
    list_[current_index], list_[index_of_smallest_value] = list_[index_of_smallest_value], list_[current_index]


def bubble_sort(list_):
  length = len(list_)

  for iteration_count in range(length):
    swapped = False

    # Compare neighboring values in the unsorted part of the list.
    for current_index in range(length - iteration_count - 1):
      if list_[current_index] > list_[current_index + 1]:
        # If the current element is greater than the next element, swap places
        list_[current_index], list_[current_index + 1] = list_[current_index + 1], list_[current_index]
        swapped = True
    if not swapped:
      break

def insertion_sort(list_):
