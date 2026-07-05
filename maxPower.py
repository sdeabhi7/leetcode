#   author: sdeabhi



def maxPower(s):
    value = 0
    n = len(s) - 1
    k = 1
    for i in range(n):
        if s[i] == s[i+1]:
            k += 1
        else:
            k = 1
        value = max(value, k)
    return value if len(s) != 1 else 1

print(maxPower('leetcode'))