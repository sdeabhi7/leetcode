#   author: sdeabhi



def sumOfSquares(nums):
    return sum(nums[i-1] * nums[i-1] for i in range(1,len(nums)+1) if len(nums) % i == 0)

print(sumOfSquares([1,2,3,4]))

# def sumOfSquares(nums):
#     k, n = 0, len(nums)
#     for i in range(1,n+1):
#         if n % i == 0:
#             k += nums[i-1] * nums[i-1]
#     return k