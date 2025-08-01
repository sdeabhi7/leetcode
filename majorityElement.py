'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''

def majorityElement(nums):
    k = 1
    value = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == value:
            k += 1
        elif k != 0:
            k -= 1
        else:
            value = nums[i]
            k = 1
    return value
    
print(majorityElement([3,2,3]))

# def majorityElement(nums):
#     return sorted(nums)[int(len(nums)/2)]