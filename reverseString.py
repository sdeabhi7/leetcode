'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:
1 <= s.length <= 10**5
s[i] is a printable ascii character.
'''

def reverseString(s):
    l = 0
    h = len(s) - 1
    while l < h:
        s[l], s[h] = s[h], s[l]
        l += 1
        h -= 1
    return s

print(reverseString(["h","e","l","l","o"]))