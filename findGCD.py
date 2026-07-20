#   author: sdeabhi



def findGCD(nums):
    l = min(nums)
    h = max(nums)
    i = l
    while i > 0:
        if l % i == 0 and h % i == 0:
            return i
        i -= 1

print(findGCD([2,5,6,9,10]))