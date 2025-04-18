'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:
Input: n = 13
Output: 6

Example 2:
Input: n = 0
Output: 0

Constraints:
0 <= n <= 109
'''

def countDigitOne(n):
    count = 0
    multiplier = 1
    while multiplier <= n:
        divider = multiplier * 10
        count += (n // divider) * multiplier
        count += min(max(n % divider - multiplier + 1, 0), multiplier)
        multiplier *= 10
    return count

print(countDigitOne(1000000000))

# def countDigitOne(n):
#     return sum(str(i).count('1') for i in range(n+1))