def firstMissingPositive(nums):
    nums, i = set(nums), 1
        while i in nums:
            i += 1
        return i  
     
print(firstMissingPositive([10]))