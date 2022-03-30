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
