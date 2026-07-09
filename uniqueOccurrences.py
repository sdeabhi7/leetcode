#   author: sdeabhi



from collections import Counter

def uniqueOccurrences(arr):
    value = Counter(arr)
    k = []
    for i in value.values():
        if i in k:
            return False
        else:
            k.append(i)
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))