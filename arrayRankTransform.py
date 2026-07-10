#   author: sdeabhi



def arrayRankTransform(arr):
    value = sorted(set(arr))
    k = {}
    for i, j in enumerate(value):
        k[j] = i + 1
    return [k[i] for i in arr]

print(arrayRankTransform([40,10,20,30]))