def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda a: (a[0], -a[1]))
    k = 0
    value = 0
    for i, j in intervals:
        if j > value:
            k += 1
            value = j
    return k

print(removeCoveredIntervals([[1,4],[3,6],[2,8]]))