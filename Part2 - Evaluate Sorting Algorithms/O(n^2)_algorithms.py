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
  length = len(list_)

  # Iterate through the list starting from the second element, treating the first element as sorted.
  for current_index in range(1, length):
    current_value = list_[current_index]
    position = current_index

    # Shift elements in the sorted part of the list to the right, as long as they're greater than the current value.
    while position > 0 and list_[position - 1] > current_value:
      list_[position] = list_[position - 1]
      position -= 1

    # Insert the current value into the correct position in the sorted part of the list.
    list_[position] = current_value