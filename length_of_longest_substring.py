def length_of_longest_substring(arr, k):
    win_start = 0
    max_occurrence = 0
    char_freq = {}
    max_length = 0
    for win_end in range(0, len(arr)):
        if arr[win_end] in char_freq:
            char_freq[arr[win_end]] += 1
        else:
            char_freq[arr[win_end]] = 1
        max_occurrence = char_freq[0]
        while max_occurrence > k:
            char_freq[arr[win_start]] -= 1
            win_start += 1
            max_occurrence = char_freq[0]
        max_length = max(max_length, win_end - win_start + 1)
    return max_length


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()
