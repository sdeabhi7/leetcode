'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
def sortedSquares(nums):
    l = 0
    r = len(nums) - 1
    value = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            value.append(nums[l] ** 2)
            l += 1
        else:
            value.append(nums[r] ** 2)
            r -= 1
    return value[::-1]
    
print(sortedSquares([-4,-1,0,3,10]))

# def sortedSquares(nums):
#     return sorted(i*i for i in nums)