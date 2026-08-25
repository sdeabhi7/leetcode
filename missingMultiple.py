#   author: sdeabhi



def missingMultiple(nums, k):
    n, i = set(nums), 1
    while True:
        if i*k not in nums:
            return i*k
        i += 1

print(missingMultiple([8,2,3,4,6], 2))

# def missingMultiple(nums, k):
#     for i in range(k, 100*k+2, k):
#         if i % k == 0 and i not in nums:
#             return i