#   author: sdeabhi



def isGood(nums):
    n = len(nums)
    nums.sort()
    return nums == list(range(1, n)) + [n - 1]

print(isGood([2, 1, 3]))