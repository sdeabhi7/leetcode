'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
 
Constraints:
1 <= arr.length <= 500
1 <= arr[i] <= 500
'''

def findLucky(arr):
    value = {}
    max_value = -1
    for i in arr:
        if i in value:
            value[i] += 1
        else:
            value[i] = 1
    for i, j in value.items():
        if i == j:
            max_value = max(i, max_value)
    return max_value

print(findLucky([2,2,3,4]))

# def findLucky(arr):
#     max_value = -1
#     for i in arr:
#         t = arr.count(i)
#         if t == i:
#             max_value = max(t, max_value)
#     return max_value