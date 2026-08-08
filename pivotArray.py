#   author: sdeabhi



def pivotArray(nums, pivot):
    l = []
    v = []
    r = []
    for i in nums:
        if i < pivot:
            l.append(i)
        elif i == pivot:
            v.append(i)
        else:
            r.append(i)
    return l + v + r

print(pivotArray([9,12,5,10,14,3,10], 10))