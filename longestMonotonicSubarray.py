#   author: sdeabhi



def longestMonotonicSubarray(nums):
    incre, m_incre, decre,  m_decre = 1, 1, 1, 1
    n = len(nums)
    for i in range(1, n):
        if nums[i-1] < nums[i]:
            incre += 1
            decre = 1
        elif nums[i-1] > nums[i]:
            decre += 1
            incre = 1
        else:
            incre = 1
            decre = 1
        m_incre = max(incre, m_incre)
        m_decre = max(decre, m_decre)
    return max(m_incre, m_decre)

print(longestMonotonicSubarray([1,4,3,3,2]))