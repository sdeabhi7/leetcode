from collections import defaultdict
from math import gcd

def countPairs(nums, k):
    count = defaultdict(int)
    ans = 0
    for num in nums:
        g = gcd(num, k)
        for prev_g in count:
            if (g * prev_g) % k == 0:
                ans += count[prev_g]
        count[g] += 1
    return ans

# def countPairs(nums, k):
#     n = len(nums)
#     value = 0
#     for i in range(n-1):
#         for j in range(i, n):
#             if i >= 0 and i < j and (nums[i] * nums[j]) % k == 0:
#                 value += 1
#     return value

print(countPairs([3,2,6,1,8,4,1], 3))

