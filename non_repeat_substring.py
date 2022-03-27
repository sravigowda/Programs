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


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccdefc")))


main()
