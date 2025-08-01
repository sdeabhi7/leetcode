'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
 
Constraints:
1 <= s.length <= 10**4
s consists of only lowercase English letters.
1 <= k <= 10**4
'''

def reverseStr(s, k):
    value = list(s)
    i, j = 0, 0
    while j < len(s):
        j += k
        value[i:j] = value[i:j][::-1]
        j += k
        i = j
    return ''.join(value)

print(reverseStr('abcdefg', 2))

# def reverseStr(s, k):
#     value = list(s)
#     h = []
#     t = ''
#     y = ''
#     for i in s:
#         t += i
#         if len(t) == k:
#             h.append(t)
#             t = ''
#     h.append(t)
#     for i in range(0, len(h)):
#         if i % 2 == 0:
#             y += h[i][::-1]
#         else:
#             y += h[i]
#     return y