def minRemoval(nums, k):
    j = 0
    n = len(nums)
    value = 0
    nums.sort()
    for i in range(n):
        while nums[i] > nums[j] * k:
            j += 1
        value = max(value, i-j+1)
    return n - value

print(minRemoval([2,1,5], 2))