def longest_substring_with_K_distinct_characters(str1, k):
    window_start = 0
    max_length = -1
    char_freq = {}

    for window_end in range(len(str1)):
        if str1[window_end] in char_freq:
            char_freq[str1[window_end]] += 1
        else:
            char_freq[str1[window_end]] = 1

        while len(char_freq) > k:
            char_freq[str1[window_start]] -= 1
            if char_freq[str1[window_start]] == 0:
                del char_freq[str1[window_start]]
            window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_K_distinct_characters("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_K_distinct_characters("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_K_distinct_characters("cbbebi", 3)))


main()
