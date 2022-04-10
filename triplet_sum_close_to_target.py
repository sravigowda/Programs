import math


def triplet_sum_close_to_target(array, targetSum):
    result = []
    triplet_close = []
    array.sort()
    print(array)
    currentSum = math.inf
    for index in range(len(array)):
        left = index+1
        right = len(array) -1
        while left < right:
            total = array[left] + array[right] + array[index]
            if total == targetSum:
                triplet_close = [array[index], array[left], array[right]]
                return sum(triplet_close)
            elif abs(targetSum - total) < currentSum:
                currentSum = targetSum - total
                triplet_close = [array[index], array[left], array[right]]
            elif total > targetSum:
                right -= 1
            else:
                left += 1

    return sum(triplet_close)



array_sum = [-2, 0, 1, 2]
print(triplet_sum_close_to_target(array_sum, 2))
array_sum = [-3, -1, 1, 2]
print(triplet_sum_close_to_target(array_sum, 1))
array_sum = [1, 0, 1, 1]
print(triplet_sum_close_to_target(array_sum, 100))
