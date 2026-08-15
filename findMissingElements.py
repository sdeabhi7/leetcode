#   author: sdeabhi




def findMissingElements(nums):
    value = []
    min_n = min(nums)
    max_n = max(nums)
    for i in range(min_n, max_n):
        if i not in nums:
            value.append(i)
    return value

print(findMissingElements([1,4,2,5]))