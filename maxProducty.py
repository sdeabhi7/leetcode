#   author: sdeabhi



def maxProduct(nums):
    nums.sort()
    return (nums[-2] - 1) * (nums[-1] - 1)

print(maxProduct([3,4,5,2]))