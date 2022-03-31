import itertools


def find_permutation(str, pattern):
    perm_list = itertools.permutations(pattern,3)
    for p in perm_list:
        new_str = "".join(p)
        if new_str in str:
            return True
    return False

def find_string(str,pattern):
    char_freq = {}
    matches = 0
    for char in pattern:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    # print(char_freq)
    for index in range(len(str)):
        if str[index] in char_freq:
            matches += 1
            if matches == len(pattern):
                return True
        else:
            matches = 0
    return False


def find_permutation_sol(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False

def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

    print('Permutation exist: ' + str(find_string("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_string("odicf", "dc")))
    print('Permutation exist: ' + str(find_string("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_string("aaacb", "abc")))


main()
