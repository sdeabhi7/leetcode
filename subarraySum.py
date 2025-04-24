'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10**4
-1000 <= nums[i] <= 1000
-10**7 <= k <= 10**7
'''

def subarraySum(nums, k):
    sum_value = {0: 1}
    current_sum = 0
    value = 0
    for num in nums:
        current_sum += num
        if (current_sum - k) in sum_value:
            value += sum_value[current_sum - k]
        sum_value[current_sum] = sum_value.get(current_sum, 0) + 1
    return value

print(subarraySum([1,1,1], 2))

# def subarraySum(nums, k):
#     value = 0
#     for i in range(len(nums)+1):
#         for j in range(i+1, len(nums)+1):   
#             if sum(nums[i:j]) == k:
#                 value += 1
#     return value