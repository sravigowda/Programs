def fruits_into_baskets(str1):
    tree_start = 0
    max_size = 0
    fruit_freq = {}
    k = 2

    for tree_end in range(len(str1)):
        if str1[tree_end] in fruit_freq:
            fruit_freq[str1[tree_end]] += 1
        else:
            fruit_freq[str1[tree_end]] = 1

        while len(fruit_freq) > k:
            fruit_freq[str1[tree_start]] -= 1
            if fruit_freq[str1[tree_start]] == 0:
                del fruit_freq[str1[tree_start]]
            tree_start += 1
        max_size = max(max_size, tree_end - tree_start +1)
    return max_size

def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

