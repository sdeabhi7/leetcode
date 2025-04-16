def mergeArrays(nums1, nums2):
    value = {}
    temp = nums1 + nums2
    for pair in temp:
        i, j = pair
        if i in value:
            value[i] += j
        else:
            value[i] = j
    return [[k, value[k]] for k in sorted(value)]

print(mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))