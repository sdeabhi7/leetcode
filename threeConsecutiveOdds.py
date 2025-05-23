'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 
Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
'''

def threeConsecutiveOdds(arr):
    if len(arr) == 3:
        return arr[0] % 2 != 0 and arr[1] % 2 != 0 and arr[2] % 2 != 0
    for i in range(len(arr)-2):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
            return True
    return False

print(threeConsecutiveOdds([2,6,4,1]))