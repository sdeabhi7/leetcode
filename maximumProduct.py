'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
 
Constraints:
3 <= nums.length <= 10**4
-1000 <= nums[i] <= 1000
'''

def maximumProduct(nums):
    nums.sort()
    i = nums[-1] * nums[-2] * nums[-3]
    j = nums[0] * nums[1] * nums[-1]
    return max(i, j)

print(maximumProduct([1,2,3]))