def insert(intervals, new_interval):
    merged = []
    for i in range(0, len(intervals)):
        if intervals[i][0] > new_interval[0]:
            intervals.insert(i, new_interval)
            break
    if i == len(intervals) - 1:
        intervals.append(new_interval)
    print(intervals)
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            merged.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
    #print(merged)
    # add the last interval
    merged.append([start, end])

    return merged

def newinsert(intervals, new_interval):
    merged = []
    start, end, i = 0, 1, 0

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1
    print(intervals)
    #merge all intervals that overlap with the new interval

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    #insert the new interval
    merged.append(new_interval)

    #insert the remaining intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged




def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [2, 4]], [3, 10])))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Intervals after inserting the new interval: " + str(newinsert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(newinsert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(newinsert([[2, 3], [5, 7]], [1, 4])))
    print("Intervals after inserting the new interval: " + str(newinsert([[1, 3], [2, 4]], [3, 10])))


main()
