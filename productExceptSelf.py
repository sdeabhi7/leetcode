'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 10**5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

def productExceptSelf(nums):
    t = len(nums)
    l = [0] * t
    r = [0] * t
    left = 1
    right = 1
    for i in range(t):
        j = -i -1
        l[i] = left
        r[j] = right
        left *= nums[i]
        right *= nums[j]
    return [i * j for i, j in zip(l, r)]

print(productExceptSelf([1,2,3,4]))

# def productExceptSelf(nums):
    # l = [1]
    # r = [1]
    # temp = 1
    # for i in range(1, len(nums)):
    #     l.append(l[i-1] * nums[i-1])
    # for i in range(len(nums)-1, 0, -1):
    #     temp *= nums[i]
    #     r.append(temp)
    # return [i * j for i, j in zip(l, r[::-1])]