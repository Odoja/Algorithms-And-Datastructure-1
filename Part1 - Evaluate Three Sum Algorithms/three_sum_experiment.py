import math
import time
import matplotlib.pyplot as plt

from three_sum_problem import threesum_brute, threesum_cache
from helpers import generate_random_list


def measure_time(function, values):
	start_time = time.perf_counter()
	function(values)
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


def test_correctness():
	for test_number in range(3):
		values = generate_random_list(15, 15)
		brute_result = sorted(threesum_brute(values))
		cache_result = sorted(threesum_cache(values))

		print("List", test_number + 1, ":", values)
		print("Brute:", brute_result)
		print("Cache:", cache_result)
		print("Same result:", brute_result == cache_result)
		print()


def run_experiments():
	sizes = [50 + 25 * index for index in range(15)]
	brute_runs = []
	cache_runs = []

	for run_number in range(3):
		brute_times = []
		cache_times = []

		for size in sizes:
			values = generate_random_list(size, size)
			brute_times.append(measure_time(threesum_brute, values))
			cache_times.append(measure_time(threesum_cache, values))

		brute_runs.append(brute_times)
		cache_runs.append(cache_times)
		print("Finished run", run_number + 1)

	brute_average = [sum(times) / 3 for times in zip(*brute_runs)]
	cache_average = [sum(times) / 3 for times in zip(*cache_runs)]

	plt.figure("Figure 1")
	for run_number in range(3):
		plt.plot(sizes, brute_runs[run_number], "o-", label="Brute run " + str(run_number + 1))
		plt.plot(sizes, cache_runs[run_number], "x--", label="Cache run " + str(run_number + 1))
	plt.xlabel("Input size n")
	plt.ylabel("Execution time (seconds)")
	plt.title("Three separate runs")
	plt.legend()
	plt.grid()

	plt.figure("Figure 1a")
	plt.plot(sizes, brute_average, "o-", label="Brute average")
	plt.plot(sizes, cache_average, "x--", label="Cache average")
	plt.xlabel("Input size n")
	plt.ylabel("Average execution time (seconds)")
	plt.title("Average time of three runs")
	plt.legend()
	plt.grid()

	log_sizes = [math.log(size) for size in sizes]
	log_brute_times = [math.log(value) for value in brute_average]
	log_cache_times = [math.log(value) for value in cache_average]

	brute_m, brute_k = lin_reg(log_sizes, log_brute_times)
	cache_m, cache_k = lin_reg(log_sizes, log_cache_times)

	print("Brute coefficient k:", brute_k)
	print("Cache coefficient k:", cache_k)

	plt.figure("Figure 2b")
	plt.scatter(log_sizes, log_brute_times, label="Brute data")
	plt.plot(log_sizes, [brute_m + brute_k * value for value in log_sizes], label="Brute fit")
	plt.scatter(log_sizes, log_cache_times, label="Cache data")
	plt.plot(log_sizes, [cache_m + cache_k * value for value in log_sizes], label="Cache fit")
	plt.xlabel("log(n)")
	plt.ylabel("log(time)")
	plt.title("Log-log data and linear regression")
	plt.legend()
	plt.grid()
	plt.show()


def main():
	test_correctness()
	run_experiments()

main()