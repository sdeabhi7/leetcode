#   author: sdeabhi



def smallestNumber(n, t):
    for i in range(n, n+10):
        s = list(str(i))
        k = 1
        for j in s:
            k *= int(j)
        if k % t == 0:
            return i

print(smallestNumber(10, 2))