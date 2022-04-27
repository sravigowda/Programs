def find_missing_numbers(nums):
    missingNumbers = []
    nums_arr = [-1] * len(nums)
    for index in range(len(nums)):
        j = nums[index]
        nums_arr[j - 1] = j
    for index in range(len(nums_arr)):
        if nums_arr[index] == -1:
            missingNumbers.append(index + 1)
    return missingNumbers


def find_missing_numbers_sol(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    print(nums)
    missingNumbers = []

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))

    print(find_missing_numbers_sol([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers_sol([2, 4, 1, 2]))
    print(find_missing_numbers_sol([2, 3, 2, 1]))


main()
