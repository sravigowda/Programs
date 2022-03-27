def non_repeat_substring(s1):
    max_length = 0
    char_count = {}

    for index in range(len(s1)):
        if s1[index] not in char_count:
            char_count[s1[index]] = 1
        else:
            max_length = max(max_length, len(char_count))
            char_count = {s1[index]: 1}
    return max(max_length, len(char_count))

# Following solution is using sliding windows technique
def no_repeat_substring(s1):
    max_length = 0
    char_index = {}
    window_start = 0
    for window_end in range(len(s1)):
        if s1[window_end] in char_index:
            window_start = max(window_start, char_index[s1[window_end]] + 1)
        char_index[s1[window_end]] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccdefc")))
    
    print("Length of the longest substring: " + str(no_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(no_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(no_repeat_substring("abccdefc")))



main()
