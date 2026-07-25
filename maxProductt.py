#   author: sdeabhi



def maxProduct(n):
    nums = sorted(str(n))
    return int(nums[-2]) * int(nums[-1])

print(maxProduct(31))