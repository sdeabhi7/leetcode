#   author: sdeabhi



def findLUSlength(a, b):
    if a not in b and len(a) > len(b):
        return len(a)
    elif b not in a and len(b) > len(a):
        return len(b)
    elif a != b and len(a) == len(b):
        return len(a)
    else:
        return -1
    
print(findLUSlength('aba', 'cdc'))