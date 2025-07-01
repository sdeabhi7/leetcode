'''
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

Constraints:
-10**7 <= num <= 10**7
'''

def convertToBase7(num):
    if num == 0:
        return '0'
    value = []
    y = '' if num > 0 else '-'
    num = abs(num)
    while num:
        value.append(str(num % 7))
        num //= 7
    return y + ''.join(value[::-1])

print(convertToBase7(100))