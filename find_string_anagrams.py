def find_string_anagrams(str1, pattern):
    window_start = 0
    char_frequency = {}
    matched = 0
    anagrams = []

    for char in pattern:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for window_end in range(len(str1)):
        if str1[window_end] in char_frequency:
            char_frequency[str1[window_end]] -= 1
            if char_frequency[str1[window_end]] == 0:
                matched += 1

        if matched == len(char_frequency):
            anagrams.append(window_start)

        if window_end >= len(pattern) - 1:
            if str1[window_start] in char_frequency:
                if char_frequency[str1[window_start]] == 0:
                    char_frequency[str1[window_start]] += 1
                    matched -= 1
            window_start += 1

    return anagrams


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
