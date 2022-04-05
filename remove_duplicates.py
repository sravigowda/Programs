def remove_duplicates(arr):
    win_start = 0
    win_end = 1

    while win_end < len(arr):
        if arr[win_start] == arr[win_end]:
            arr.pop(win_end)
        else:
            win_start += 1
            win_end += 1
    return len(arr)


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
