#   author: sdeabhi



def firstStableIndex(nums, k):
    n = len(nums)
    h = float('inf')
    value = float('inf')
    for i in range(n):
        value = max(nums[:i+1]) - min(nums[i:])
        if value <= k:
            h = min(i, h)
    return h if h <= n else -1

print(firstStableIndex([5,0,1,4], 3))