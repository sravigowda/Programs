def remove_element(arr, key):
    win_start = 0
    while win_start < len(arr):
        if arr[win_start] == key:
            arr.pop(win_start)
        else:
            win_start += 1
    return len(arr)


def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))


main()
