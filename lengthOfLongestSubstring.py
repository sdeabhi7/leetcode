'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestSubstring(s):
    l = 0
    value = set()
    max_len = 0
    for i in range(len(s)):
        while s[i] in value:
            value.remove(s[l])
            l += 1
        value.add(s[i])
        max_len = max(max_len, len(value))
    return max_len

print(lengthOfLongestSubstring('abcabcbb'))