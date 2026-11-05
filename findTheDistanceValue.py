#   author: sdeabhi



def findTheDistanceValue(arr1, arr2, d):
    value = 0
    for i in arr1:
        for j in arr2:
            if abs(i-j) <= d:
                value += 1
                break
    return len(arr1) - value

print(findTheDistanceValue([4,5,8], [10,9,1,8], 2))