'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 10**5
ransomNote and magazine consist of lowercase English letters
'''

def canConstruct(ransomNote, magazine):
    value = {}
    for i in magazine:
        if i in value:
            value[i] += 1
        else:
            value[i] = 1
    for i in ransomNote:
        if i in value and value[i] != 0:
            value[i] -= 1
        else:
            return False
    return True

print(canConstruct('a', 'b'))