'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10**4
intervals[i].length == 2
0 <= starti <= endi <= 10**4
'''

def merge(intervals):
    if not intervals:
        return [] 
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  
            last[1] = max(last[1], current[1])
            print(f'last - {last}')
            print(f'merged - {merged}')
        else:
            merged.append(current)
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))