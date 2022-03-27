def max_sub_array_of_size_k(k, arr):
    total = 0
    max_total = 0
    win_start = 0
    for win_end in range(len(arr)):
        total += arr[win_end]
        if win_end - win_start + 1 > k:
            total -= arr[win_start]
            win_start += 1
        max_total = max(max_total, total)
    return max_total

# Brute Force Approach

def max_sub_array_of_size_k_new(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_new(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_new(2, [2, 3, 4, 1, 5])))


main()
