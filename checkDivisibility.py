#   author: sdeabhi



def checkDivisibility(n):
    nums = str(n)
    s, p = 0, 1
    for i in nums:
        s += int(i)
        p *= int(i)
    return (n % (s+p)) == 0

print(checkDivisibility(99))