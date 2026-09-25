import math
import time

import matplotlib.pyplot as plt

from nlogn_algorithms import merge_sort, quick_sort
from special_case_algorithms import bucket_sort, radix_sort
from helpers import generate_random_list


def measure_time(sort_function, values):
  values_copy = values.copy()
  start_time = time.perf_counter()
  sort_function(values_copy)
  return time.perf_counter() - start_time


def lin_reg(x, y):
  x_mean = sum(x) / len(x)
  y_mean = sum(y) / len(y)

  numerator = sum(
    (x_value - x_mean) * (y_value - y_mean)
    for x_value, y_value in zip(x, y)
  )
  denominator = sum((x_value - x_mean) ** 2 for x_value in x)

  k = numerator / denominator
  m = y_mean - k * x_mean
  return m, k


def run_experiment():
  sizes = [100 + 100 * index for index in range(15)]
  algorithms = [merge_sort, quick_sort, bucket_sort, radix_sort]
  runs = {algorithm.__name__: [] for algorithm in algorithms}

  for run_number in range(3):
    for algorithm in algorithms:
      times = []

      for size in sizes:
        values = generate_random_list(size, size)
        times.append(measure_time(algorithm, values))

      runs[algorithm.__name__].append(times)

    print("Run", run_number + 1, "completed")

  averages = {}
  coefficients = {}

  for algorithm in algorithms:
    name = algorithm.__name__
    averages[name] = [sum(times) / 3 for times in zip(*runs[name])]

    log_sizes = [math.log2(size) for size in sizes]
    log_times = [math.log2(value) for value in averages[name]]
    m, k = lin_reg(log_sizes, log_times)
    coefficients[name] = (m, k)
    print(name, "k =", k)

  plt.figure("Figure 1")
  for algorithm in algorithms:
    name = algorithm.__name__
    plt.plot(sizes, averages[name], marker="o", label=name)
  plt.xlabel("List sizes in range 100 to 1500")
  plt.ylabel("Average time of 3 runs with random lists")
  plt.title("Running times for special case algorithms vs O(n*log(n)) algorithms")
  plt.legend()
  plt.grid()

  plt.figure("Figure 2")
  log_sizes = [math.log2(size) for size in sizes]

  for algorithm in algorithms:
    name = algorithm.__name__
    log_times = [math.log2(value) for value in averages[name]]
    m, k = coefficients[name]
    plt.plot(log_sizes, log_times, marker="o", label=name + " k = " + format(k, ".3f"))

  plt.xlabel("Log2 of list sizes")
  plt.ylabel("Log2 of sorting times")
  plt.title("Log-log plots for special case algorithms vs O(n*log(n)) algorithms")
  plt.legend()
  plt.grid()
  plt.show()


def main():
  run_experiment()


main()