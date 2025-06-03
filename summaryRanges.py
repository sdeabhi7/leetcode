'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:
0 <= nums.length <= 20
-2**31 <= nums[i] <= 2**31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''

def summaryRanges(nums):
    value = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        end = nums[i]
        if start == end:
            value.append(str(start))
        else:
            value.append(f"{start}->{end}")
        i += 1
    return value
    
print(summaryRanges([0,1,2,4,5,7]))

# def summaryRanges(nums):
    # if len(nums) != 0:   
    #     value = []
    #     k = []  
    #     for i in range(nums[0], nums[-1] + 2):
    #         if i in nums:
    #             k.append(i)
    #         else:
    #             if len(k) == 1:
    #                 value.append(str(k[0]))
    #                 k = []
    #             elif len(k) == 0:
    #                 continue
    #             else:
    #                 temp = ''
    #                 temp = str(k[0]) + '->' + str(k[-1])
    #                 value.append(temp)
    #                 k = []
    #     return value
    # else:
    #     return nums