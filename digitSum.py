#   author: sdeabhi



def digitSum(s, k):
    while len(s) > k:
        n = len(s)
        r = ''
        for i in range(0,n,k):
            y = list(s[i:i+k])
            r += str(sum(int(j) for j in y))
        s = r
    return s

print(digitSum('11111222223', 3))