'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

def numberOfSubstrings(s):
    substrs = 0
    last_pos = [-1] * 3
    for pos in range(len(s)):
        last_pos[ord(s[pos]) - ord("a")] = pos
        substrs += 1 + min(last_pos)
    return substrs

# def numberOfSubstrings(s):
#     temp = 0
#     for i in range(len(s)-2):
#         for j in range(i, len(s)-2):
#             v = 3+j
#             if v <= len(s):
#                 k = s[i:3+j]
#                 y = ''.join(list(set(k)))
#                 abc_count = sum(1 for i in y if i in 'abc')
#                 if abc_count >= 3:
#                     temp += 1
#     return temp