#   author: sdeabhi



def targetIndices(nums, target):
    nums.sort()
    return [i for i in range(len(nums)) if nums[i] == target]

print(targetIndices([1,2,5,2,3], 2))
