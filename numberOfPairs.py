#   author: sdeabhi




def numberOfPairs(nums1, nums2, k):
    value = 0
    for i in nums1:
        for j in nums2:
            if i % (j * k) == 0:
                value += 1
    return value

print(numberOfPairs([1,3,4], [1,3,4], 1))