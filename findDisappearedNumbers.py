'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
 
Constraints:
n == nums.length
1 <= n <= 10**5
1 <= nums[i] <= n
 
Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''

def findDisappearedNumbers(nums):
    value = []
    n = len(nums) + 1
    k = [0] * n
    for i in nums:
        k[i] = 1
    for j in range(1, n):
        if k[j] == 0:
            value.append(j)
    return value

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))

# def findDisappearedNumbers(nums):
    # value = []
    # n = len(nums)
    # for i in range(1, n + 1):
    #     if i not in nums:
    #         value.append(i)
    # return value

# print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))