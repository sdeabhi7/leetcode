'''
You are given two strings s1 and s2 of equal length. 
A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 
Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
'''

def areAlmostEqual(s1, s2):
    s = list(s1)
    y = list(s2)
    s.sort()
    y.sort()
    if ''.join(s) == ''.join(y):
        s1_new = {}
        s2_new = {}
        temp = []
        for i, j in enumerate(s1):
            s1_new[i] = j
        for i, j in enumerate(s2):
            s2_new[i] = j
        for i in range(len(s1_new)):
            if s1_new[i] != s2_new[i]:
                temp.append(i)
        return len(set(temp)) <= 2
    return False


print(areAlmostEqual("bank", "kanb"))

# def areAlmostEqual(s1, s2):
    # if s1 == s2:
    #     return True
    # s = sorted(list(s1))
    # y = sorted(list(s2))
    # if ''.join(s) != ''.join(y):
    #     return False
    # else:
    #     temp = 0
    #     for i, j in zip(s1,s2):
    #         if i != j:
    #             temp += 1
    # return temp <= 2
