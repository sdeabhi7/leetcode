#   author: sdeabhi



def minMoves(nums):
    max_value, value = max(nums), 0
    for i in nums:
        value += max_value - i
    return value

print(minMoves([2,1,3]))