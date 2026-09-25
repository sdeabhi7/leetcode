#   author: sdeabhi




def reverseDegree(s):
    y = 'abcdefghijklmnopqrstuvwxyz'
    r = y[::-1]
    k = 0
    t = len(s)
    for i in range(t):
        k += (r.find(s[i]) + 1) * (i+1)
    return k

print(reverseDegree('abc'))