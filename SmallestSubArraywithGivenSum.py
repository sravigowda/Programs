import math


def smallest_subarray_with_given_sum(s,array):
    window_start = 0
    window_sum = 0
    min_length = math.inf
    for window_end in range(0, len(array)):
        window_sum += array[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= array[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    else:
        return min_length
    


print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
