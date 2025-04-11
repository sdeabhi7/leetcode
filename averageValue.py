'''
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

Example 1:
Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

Example 2:
Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
'''

def averageValue(nums):
    value = [i for i in nums if i % 3 == 0 and i % 2 == 0]
    return int(sum(value)/len(value)) if value else 0

print(averageValue([1,3,6,10,12,15]))