def cyclic_sort(nums):
    for index in range(len(nums) - 1):
        if nums[index] == index + 1:
            continue
        else:
            while nums[index] != index + 1:
                j = nums[index] - 1
                nums[index], nums[j] = nums[j], nums[index]
                print(nums)
    return nums


def new_cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print("######")
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print("######")
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))
    print("######")
    print(new_cyclic_sort([3, 1, 5, 4, 2]))
    print("######")
    print(new_cyclic_sort([2, 6, 4, 3, 1, 5]))
    print("######")
    print(new_cyclic_sort([1, 5, 6, 4, 3, 2]))
    print("######")

main()
