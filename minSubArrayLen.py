'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''

def minSubArrayLen(target, nums):
    min_len = float("inf")
    left = 0
    cur_sum = 0

    for right in range(len(nums)):
        cur_sum += nums[right]

        while cur_sum >= target:
            if right - left + 1 < min_len:
                min_len = right - left + 1
            cur_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float("inf") else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))

# def minSubArrayLen(target, nums):
#     value = len(nums)
#     if sum(nums) == target:
#         return value
#     if sum(nums) > target:
#         for i in range(len(nums)):
#             for j in range(i, len(nums)+1):
#                 if sum(nums[i:j]) >= target and len(nums[i:j]) < value:
#                     value = len(nums[i:j])
#         return value
#     else:
#         return 0

# print(minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))


