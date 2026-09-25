def selection_sort(list_):

def bubble_sort(list_):
  length = len(list_)

  for iteration_count in range(length):
    swapped = False
    for current_index in range(length - iteration_count - 1):
      if list_[current_index] > list_[current_index + 1]:
        # If the current element is greater than the next element, swap places
        list_[current_index], list_[current_index + 1] = list_[current_index + 1], list_[current_index]
        swapped = True
    if not swapped:
      break

def insertion_sort(list_):
