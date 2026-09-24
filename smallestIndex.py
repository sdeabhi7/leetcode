#   author: sdeabhis



def smallestIndex(nums):
    n = len(nums)
    k = 0
    for i in range(n):
        k = sum(int(i) for i in str(nums[i]))
        if k == i:
            return k
    return -1

print(smallestIndex([1,3,2]))