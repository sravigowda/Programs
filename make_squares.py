import math


def make_squares(arr):
    squares = []
    index = 0
    positive = math.inf
    negative = math.inf
    while arr[index] < 0:
        index += 1

    if arr[index] == 0:
        positive = index + 1
        negative = index - 1
        squares.append(0)
    else:
        negative = index - 1
        positive = index

    while positive < len(arr) and negative >= 0:
        if arr[positive] ** 2 == arr[negative] ** 2:
            squares.append(arr[negative] ** 2)
            squares.append(arr[positive] ** 2)
            positive += 1
            negative -= 1
        elif arr[positive] ** 2 > arr[negative] ** 2:
            squares.append(arr[negative] ** 2)
            negative -= 1
        else:
            squares.append(arr[positive] ** 2)
            positive += 1

    while positive < len(arr):
        squares.append((arr[positive] ** 2))
        positive += 1
    while negative >= 0:
        squares.append((arr[negative] ** 2))
        negative -= 1

    return squares


def make_squares_new(arr):
    n = len(arr)
    left = 0
    right = n - 1
    highestindex = n - 1

    square = [0 for x in range(n)]
    while left <= right:
        leftsquare = arr[left] ** 2
        rightsquare = arr[right] ** 2
        if rightsquare > leftsquare:
            square[highestindex] = rightsquare
            right -= 1
        else:
            square[highestindex] = leftsquare
            left += 1
        highestindex -= 1

    return square




def main():
    print("Squares: " + str(make_squares([-4, -2, -1, 0, 2, 3, 4, 5])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
    print("Squares: " + str(make_squares_new([-4, -2, -1, 0, 2, 3, 4, 5])))
    print("Squares: " + str(make_squares_new([-3, -1, 0, 1, 2])))


main()
