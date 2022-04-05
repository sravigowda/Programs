def pair_with_targetsum(arr, target_sum):
    win_start = 0
    win_end = len(arr) - 1
    print(win_end, win_start)
    while win_start < win_end:
        if arr[win_start] + arr[win_end] > target_sum:
            win_end -= 1
        elif arr[win_start] + arr[win_end] < target_sum:
            win_start += 1
        elif arr[win_start] + arr[win_end] == target_sum:
            return [win_start, win_end]
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
