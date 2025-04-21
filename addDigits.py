'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1
'''

def addDigits(num):
    if len(str(num)) == 1:
        return num
    else:
        k = str(num)
        while len(k) > 1:
            temp = 0
            for i in k:
                temp += int(i)
            k = str(temp)
    return temp

print(addDigits(38))

# def addDigits(num):
#     if num == 0:
#         return 0
#     else:
#         if num % 9 == 0:
#             return 9
#         else:
#             return num % 9 
        
