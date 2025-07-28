def countHillValley(nums):
    v = 0
    h = 0
    value = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            value.append(nums[i])
    for i in range(1, len(value) - 1):
        if value[i-1] < value[i] > value[i+1]:
            h += 1
        elif value[i-1] > value[i] < value[i+1]:
            v += 1
    return h + v

print(countHillValley([2,4,1,1,6,5]))